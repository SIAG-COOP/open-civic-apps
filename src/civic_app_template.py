#!/usr/bin/env python3

"""
Plantilla base para aplicaciones cívicas abiertas – SIAG COOP

Esta plantilla proporciona:
- estructura mínima para iniciar una app cívica
- interfaz por línea de comandos (CLI)
- descripción integrada
"""

import argparse

def run_demo():
    print("🌱 Aplicación Cívica SIAG COOP en ejecución (modo demo).")

def main():
    parser = argparse.ArgumentParser(
        description="Plantilla base para aplicaciones cívicas abiertas (SIAG COOP)"
    )
    parser.add_argument("--demo", action="store_true", help="Ejecutar en modo demo")
    args = parser.parse_args()

    if args.demo:
        run_demo()
    else:
        print("Iniciando aplicación cívica... (placeholder)")

if __name__ == "__main__":
    main()
