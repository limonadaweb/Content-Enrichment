Feature: Calculator
Scenario: Traducir texto de entrada
Given Tengo un texto de input
And tengo un código ISO del idioma de origen
And tengo un código ISO del idioma de destino
When llamo al método de traducción
Then tengo un texto traducido

Scenario: Traducir texto de entrada
Given Tego un texto de input no valido
And tengo un código ISO del idioma de origen
And tengo un código ISO del idioma de destino
When llamo al método de traducción
Then tira una exception de tipo

Scenario: Traducir texto de entrada
Given Tego un texto de input
And tengo un código ISO del idioma de origen
And tengo un código ISO del idioma de destino
When llamo al método de traducción
Then tengo un texto traducido

Scenario: Traducir texto de entrada
Given Tego un texto de input
And tengo un código ISO del idioma de origen
And tengo un código ISO del idioma de destino
When llamo al método de traducción
Then tengo un texto traducido
