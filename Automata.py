# Automata.py

def check_string(s):
    # Estado inicial: q0
    state = 'q0'
    
    for char in s:
        if state == 'q0':
            if char == 'a':
                state = 'q1'
            elif char == 'b':
                state = 'q2'
        elif state == 'q1':
            if char == 'a':
                state = 'q0'
            elif char == 'b':
                state = 'q3'
        elif state == 'q2':
            if char == 'a':
                state = 'q3'
            elif char == 'b':
                state = 'q0'
        elif state == 'q3':
            if char == 'a':
                state = 'q2'
            elif char == 'b':
                state = 'q1'

    # El estado de aceptación es q1
    if state == 'q1':
        return "Cadena aceptada"
    else:
        return "Cadena rechazada"

# Ejemplo de uso
if __name__ == "__main__":
    cadena = input("Introduce una cadena de caracteres (solo 'a' y 'b'): ")
    resultado = check_string(cadena)
    print(resultado)
