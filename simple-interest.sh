#!/bin/bash
# Cálculo de interés simple
principal=1000
rate=5
time=2
interest=$((principal * rate * time / 100))
echo "El interés simple es: $interest"
