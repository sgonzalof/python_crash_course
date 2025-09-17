import sqlite3
from typing import List, Tuple, Optional

class DatabaseManager:
    def __init__(self, db_name: str):
        """Inicializar conexión a la base de datos"""
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        """Establecer conexión a la base de datos"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f"✅ Conexión establecida con {self.db_name}")
        except sqlite3.Error as e:
            print(f"❌ Error conectando a la base de datos: {e}")

    def disconnect(self):
        """Cerrar conexión a la base de datos"""
        if self.conn:
            self.conn.close()
            print("🔌 Conexión cerrada")

    def create_tables(self):
        """Crear tablas si no existen"""
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                email TEXT UNIQUE
            )
            """)
            self.conn.commit()
            print("📋 Tabla 'students' creada correctamente")
        except sqlite3.Error as e:
            print(f"❌ Error creando tabla: {e}")

    # CREATE - Insertar datos
    def create_student(self, name: str, age: int, email: str) -> bool:
        """Insertar un nuevo estudiante"""
        try:
            self.cursor.execute("""
            INSERT INTO students (name, age, email) 
            VALUES (?, ?, ?)
            """, (name, age, email))
            self.conn.commit()
            print(f"➕ Estudiante {name} añadido correctamente")
            return True
        except sqlite3.IntegrityError:
            print(f"❌ Error: El email {email} ya existe")
            return False
        except sqlite3.Error as e:
            print(f"❌ Error insertando estudiante: {e}")
            return False

    # READ - Leer datos
    def read_all_students(self) -> List[Tuple]:
        """Obtener todos los estudiantes"""
        try:
            self.cursor.execute("SELECT * FROM students")
            students = self.cursor.fetchall()
            print("📖 Listado de estudiantes:")
            for student in students:
                print(f"ID: {student[0]}, Nombre: {student[1]}, Edad: {student[2]}, Email: {student[3]}")
            return students
        except sqlite3.Error as e:
            print(f"❌ Error leyendo estudiantes: {e}")
            return []

    def read_student(self, student_id: int) -> Optional[Tuple]:
        """Obtener un estudiante por su ID"""
        try:
            self.cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
            student = self.cursor.fetchone()
            if student:
                print(f"🔍 Estudiante encontrado: {student}")
                return student
            else:
                print(f"⚠️ No se encontró estudiante con ID {student_id}")
                return None
        except sqlite3.Error as e:
            print(f"❌ Error buscando estudiante: {e}")
            return None

    # UPDATE - Actualizar datos
    def update_student(self, student_id: int, name: str = None, age: int = None, email: str = None) -> bool:
        """Actualizar datos de un estudiante"""
        try:
            # Construir query dinámicamente basado en los campos proporcionados
            updates = []
            values = []
            if name:
                updates.append("name = ?")
                values.append(name)
            if age:
                updates.append("age = ?")
                values.append(age)
            if email:
                updates.append("email = ?")
                values.append(email)
            
            if not updates:
                print("⚠️ No se proporcionaron datos para actualizar")
                return False

            values.append(student_id)
            query = f"UPDATE students SET {', '.join(updates)} WHERE id = ?"
            
            self.cursor.execute(query, values)
            self.conn.commit()
            
            if self.cursor.rowcount > 0:
                print(f"✏️ Estudiante {student_id} actualizado correctamente")
                return True
            else:
                print(f"⚠️ No se encontró estudiante con ID {student_id}")
                return False
                
        except sqlite3.Error as e:
            print(f"❌ Error actualizando estudiante: {e}")
            return False

    # DELETE - Eliminar datos
    def delete_student(self, student_id: int) -> bool:
        """Eliminar un estudiante por su ID"""
        try:
            self.cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            self.conn.commit()
            
            if self.cursor.rowcount > 0:
                print(f"🗑️ Estudiante {student_id} eliminado correctamente")
                return True
            else:
                print(f"⚠️ No se encontró estudiante con ID {student_id}")
                return False
        except sqlite3.Error as e:
            print(f"❌ Error eliminando estudiante: {e}")
            return False

def main():
    """Función principal para demostrar el uso del CRUD"""
    # Crear instancia del gestor de base de datos
    db = DatabaseManager("school.db")
    
    # Conectar a la base de datos
    db.connect()
    
    # Crear tabla
    db.create_tables()
    
    # Ejemplos de uso
    print("\n=== CREATE ===")
    db.create_student("Juan Pérez", 20, "juan@email.com")
    db.create_student("Ana García", 22, "ana@email.com")
    
    print("\n=== READ ===")
    db.read_all_students()
    db.read_student(1)
    
    print("\n=== UPDATE ===")
    db.update_student(1, name="Juan Pablo Pérez", age=21)
    db.read_student(1)
    
    print("\n=== DELETE ===")
    db.delete_student(2)
    db.read_all_students()
    
    # Cerrar conexión
    db.disconnect()

if __name__ == "__main__":
    main()