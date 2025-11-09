# Script de inicio rápido

import subprocess
import sys

def main():
    print("=" * 60)
    print("  Sistema Inteligente de Monitoreo de Producción")
    print("=" * 60)
    print("\nIniciando la aplicación web...")
    print("\nUsuarios de prueba:")
    print("  - admin / admin123 (Administrador)")
    print("  - supervisor / super123 (Supervisor)")
    print("  - operador / oper123 (Operador)")
    print("\n" + "=" * 60)
    
    # Ejecutar streamlit
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])

if __name__ == "__main__":
    main()
