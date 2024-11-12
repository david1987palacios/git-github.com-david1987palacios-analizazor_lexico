import re  

# Definición de los tipos de tokens  
TOKEN_TYPE = [  
    ("NUMBER", r'\d+(\.\d+)?'),        # Números  
    ("IDENTIFIER", r'[a-zA-Z_]\w*'),   # Identificadores  
    ("ASSIGN", r'='),                   # Asignación  
    ("PLUS", r'\+'),                    # Suma  
    ("COMMA", r','),                    # Coma  
    ("LPAREN", r'\('),                  # Paréntesis izquierdo  
    ("RPAREN", r'\)'),                  # Paréntesis derecho  
    ("STRING", r'"[^"]*"'),             # Cadenas de texto  
    ("NEWLINE", r'\n'),                 # Nueva línea  
    ("SKIP", r'[ \t]+'),                # Espacios y tabulaciones  
    ("MISMATCH", r'.'),                 # Cualquier otro carácter no válido  
]  

# Compilar las expresiones regulares  
TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPE)  

class Lexer:  
    def __init__(self, text):  
        self.text = text  
        self.position = 0  
    
    def tokenize(self):  
        tokens = []  
        for match in re.finditer(TOKEN_REGEX, self.text):  
            token_type = match.lastgroup  
            if token_type == "NEWLINE":  
                continue  
            elif token_type == "SKIP":  
                continue  
            elif token_type == "MISMATCH":  
                raise RuntimeError(f"Unexpected character: {match.group()}")  
            else:  
                tokens.append((token_type, match.group()))  
        return tokens  

# Ejemplo de uso  
code = '''  
n1 = float(input("Intro número uno: "))  
n2 = float(input("Intro numero dos: "))  
suma = n1 + n2  
print("La suma es:", suma)  
'''  

lexer = Lexer(code)  
tokens = lexer.tokenize()  

for token in tokens:  
    print(token)
    
    #Para verificar la tabla de componentes ejecutamos "python lexer.py" en la terminal y "python practica2.py para ejecuar el codigo a anaizar"