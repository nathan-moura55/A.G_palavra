Este é um projeto em Python é um estudo inicial de **Algoritmo Genético (A.G.)** que analisa as gerações de palavra ou frase definida pelo usuário. O script inclui uma interface interativa no terminal, exibição de progresso em tempo real e uma análise gráfica final do histórico de desempenho (evolução do fitness) gerada diretamente no console.

## Como Funciona o Algoritmo Genético?

O algoritmo simula o processo de evolução natural baseado na teoria de Darwin, utilizando os seguintes conceitos:

1. **População Inicial:** Criação de um conjunto de strings aleatórias com o mesmo comprimento da palavra-alvo.
2. **Cálculo de Fitness (Aptidão):** Avaliação de cada indivíduo contando quantos caracteres estão na posição correta em relação à palavra-alvo (Distância de Hamming).
3. **Seleção:** Utiliza a técnica de **Seleção por Torneio** ($k=50$), onde indivíduos são escolhidos aleatoriamente e o melhor entre eles avança.
4. **Crossover (Cruzamento):** Combina os "genes" (caracteres) de dois pais em um ponto de corte aleatório para gerar um novo filho.
5. **Mutação Dinâmica:** Aplica alterações aleatórias nos caracteres. A taxa de mutação é inversamente proporcional ao fitness: começa alta (20%) para garantir diversidade e cai gradativamente até 2% à medida que a solução ideal se aproxima, protegendo os genes corretos.
6. **Elitismo:** O melhor indivíduo de cada geração é preservado intacto para a próxima, garantindo que o algoritmo nunca perca a melhor solução já encontrada.

---

## Expressão Algébrica do Fitness

A função de aptidão ($f$) para um indivíduo $I$ em relação à palavra-alvo $P$, ambos de comprimento $x$, pode ser expressa algebricamente através da somatória da função delta de Kronecker ($\delta$) para cada par de caracteres na mesma posição $i$:

$$f(I) = \sum_{i=1}^{x} \delta(I_i, P_i)$$

Onde:
* $I_i$ é o caractere na posição $i$ do indivíduo.
* $P_i$ é o caractere na posição $i$ da palavra-alvo.
* $\delta(I_i, P_i) = \begin{cases} 1, & \text{se } I_i = P_i \\ 0, & \text{se } I_i \neq P_i \end{cases}$

O objetivo do algoritmo é maximizar $f(I)$ até que $f(I) = x$.

---

## Tecnologias Utilizadas

* **Python 3.10+**
* Módulos nativos: `string`, `random`, `time`

---

##  Como Executar o Projeto

1. Certifique-se de ter o Python instalado na sua máquina.
2. Baixe o arquivo `GA_palavra.py`.
3. Abra o terminal na pasta do arquivo e execute:
```bash
   python GA_senha.py
```

---

## Saida do terminal

Abaixo está uma demonstração real do algoritmo a convergir para a famosa frase de Fernando Pessoa (*"Tudo vale a pena se a alma nao e pequena"*), partindo de uma população inicial 100% aleatória:

```text
Digite o texto: Tudo vale a pena se a alma nao e pequena

--- INICIANDO A.G ---
Geracao 001 | Mutação: 18.2% | Melhor: quB cVZTW1Ey3cguWX9yKv VQ6mnIt4LwxWqKe7I | Fitness: 04/40 | [██                    ]
Geracao 002 | Mutação: 17.3% | Melhor: EAxz veoQWkEDppx lTZVw4pJ-YaaS04 plx1bqt | Fitness: 06/40 | [███                   ]
Geracao 003 | Mutação: 16.0% | Melhor: irJO BkWgh6SwenA GsqP13SsrQnam4owxWque7I | Fitness: 09/40 | [████                  ]
Geracao 004 | Mutação: 15.1% | Melhor: W0d8 Bul8h6SyenA usqP13SsGQnam4kwxWque7I | Fitness: 11/40 | [█████                 ]
Geracao 005 | Mutação: 14.2% | Melhor: RAdz vhZef9GaJn6 UfGP7NFsrQnaQ0s pQqneAa | Fitness: 13/40 | [██████                ]
Geracao 006 | Mutação: 13.7% | Melhor: T0d8 Nulef9rwenA b2qJyil4rQnadWovxLque7I | Fitness: 14/40 | [███████               ]
Geracao 007 | Mutação: 12.4% | Melhor: Rvdm vuZeBN 4enE 3eG  NlX6 iadBHEp0qdewa | Fitness: 17/40 | [████████              ]
Geracao 008 | Mutação: 11.9% | Melhor: Rvdm vuZeYV 4enE 3eG  NlX6Qnam04 pesuBnN | Fitness: 18/40 | [█████████             ]
Geracao 009 | Mutação: 11.5% | Melhor: T0d8 Tulef98penk yeG  Nlz6 aaK i pKxu4n1 | Fitness: 19/40 | [█████████             ]
Geracao 010 | Mutação: 10.6% | Melhor: T0d8 TOlef98penk yeG  Nlz6 naK HEp0qzena | Fitness: 21/40 | [██████████            ]
Geracao 011 | Mutação: 9.7%  | Melhor: T0d8 Vulefa8penk Ke   NlXgQna 04 peqnena | Fitness: 23/40 | [███████████           ]
Geracao 012 | Mutação: 9.7%  | Melhor: T0d8 Vulefa8penk Ke   NlXgQna 04 peqnena | Fitness: 23/40 | [███████████           ]
Geracao 013 | Mutação: 8.8%  | Melhor: Tudp 9ulefa8penk yes  NOsa naa 4 peOuena | Fitness: 25/40 | [████████████          ]
Geracao 014 | Mutação: 8.3%  | Melhor: Tudp Tale a8penkpyeS  uOsa naV 4 pecuena | Fitness: 26/40 | [█████████████         ]
Geracao 015 | Mutação: 7.4%  | Melhor: Tpd1 valefa8penk Ke 1 NlZa naa 4 peUuena | Fitness: 28/40 | [██████████████        ]
Geracao 016 | Mutação: 7.0%  | Melhor: TudG Tale a8penk Ke 1 NlZa naa 4 peduena | Fitness: 29/40 | [██████████████        ]
Geracao 017 | Mutação: 7.0%  | Melhor: TudG Tale a8penk Ke 1 NlZa naa 4 peduena | Fitness: 29/40 | [██████████████        ]
Geracao 018 | Mutação: 6.1%  | Melhor: Tud1 valeba8penk Ke 1 Ylma naa W pequena | Fitness: 31/40 | [███████████████       ]
Geracao 019 | Mutação: 5.6%  | Melhor: Tudo vale a8penk Ke 1 Yama naa W pequena | Fitness: 32/40 | [████████████████      ]
Geracao 020 | Mutação: 5.2%  | Melhor: Tudo vale a8pena be 1 NlZa naa p pequena | Fitness: 33/40 | [████████████████      ]
Geracao 021 | Mutação: 4.7%  | Melhor: Tudo vale a8pena be 1 Ylma naa W pequena | Fitness: 34/40 | [█████████████████     ]
Geracao 022 | Mutação: 4.3%  | Melhor: Tudo vale a8penk Ke a alZa naa e pequena | Fitness: 35/40 | [█████████████████     ]
Geracao 023 | Mutação: 3.8%  | Melhor: Tudo vale aepena Ke a alZa naa e pequena | Fitness: 36/40 | [██████████████████    ]
Geracao 024 | Mutação: 3.4%  | Melhor: Tudo vale a8pena be a alma naz e pequena | Fitness: 37/40 | [██████████████████    ]
Geracao 025 | Mutação: 3.4%  | Melhor: Tudo vale a8pena be a alma naz e pequena | Fitness: 37/40 | [██████████████████    ]
Geracao 026 | Mutação: 3.4%  | Melhor: Tudo vale a8pena be a alma naz e pequena | Fitness: 37/40 | [██████████████████    ]
Geracao 027 | Mutação: 3.4%  | Melhor: Tudo vale a8pena be a alma naz e pequena | Fitness: 37/40 | [██████████████████    ]
Geracao 028 | Mutação: 2.9%  | Melhor: Tudo vale aepena Ke a alma nao e pequena | Fitness: 38/40 | [███████████████████   ]
Geracao 029 | Mutação: 2.9%  | Melhor: Tudo vale aepena Ke a alma nao e pequena | Fitness: 38/40 | [███████████████████   ]
Geracao 030 | Mutação: 2.5%  | Melhor: Tudo vale a pena be a alma nao e pequena | Fitness: 39/40 | [███████████████████   ]
Geracao 031 | Mutação: 2.5%  | Melhor: Tudo vale a pena be a alma nao e pequena | Fitness: 39/40 | [███████████████████   ]
Geracao 032 | Mutação: 2.0%  | Melhor: Tudo vale a pena se a alma nao e pequena | Fitness: 40/40 | [████████████████████]

>> Palavra encontrada na geração: 32

==================================================
       HISTORICO DE DESEMPENHO (EIXO Y)
==================================================
Fitness
40 |                                                                *
36 |                                               * * * * * * * * * *
32 |                                     * * * * * * * * * * * * * * *
28 |                             * * * * * * * * * * * * * * * * * * *
24 |                         * * * * * * * * * * * * * * * * * * * * *
20 |                   * * * * * * * * * * * * * * * * * * * * * * * *
16 |             * * * * * * * * * * * * * * * * * * * * * * * * * * *
12 |         * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
08 |     * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
04 | * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
   -----------------------------------------------------------------
    0                           Gerações (Eixo X)                           32
```


```bash
   python GA_senha.py
