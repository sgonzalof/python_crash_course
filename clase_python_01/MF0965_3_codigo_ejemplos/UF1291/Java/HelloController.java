
// UF1291 - Despliegue (Java - Spring Boot ejemplo básico)
// Nota: Este es un ejemplo simplificado de un controlador REST
// Requiere proyecto Spring Boot para funcionar.

import org.springframework.web.bind.annotation.*;

@RestController
public class HelloController {
    @GetMapping("/hello")
    public String hello() {
        return "Hello from component!";
    }
}
