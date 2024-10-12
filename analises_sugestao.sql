--# Dicionário de dados 
--
--| **Variável**                    | **Tipo**    | **Descrição**                                                                 |
--|----------------------------------|-------------|-------------------------------------------------------------------------------|
--| **Gênero**                       | Categórico  | Gênero da pessoa (Masculino, Feminino, etc.)                                  |
--| **Idade**                        | Contínuo    | Idade da pessoa                                                               |
--| **Altura**                       | Contínuo    | Altura da pessoa (em metros)                                                  |
--| **Peso**                         | Contínuo    | Peso da pessoa (em quilogramas)                                               |
--| **Histórico familiar de sobrepeso** | Binário    | Alguém na família da pessoa sofreu ou sofre de sobrepeso? (Sim/Não)           |
--| **Frequência de alimentos calóricos (FAVC)** | Binário    | A pessoa consome alimentos altamente calóricos com frequência? (Sim/Não)      |
--| **Consumo de vegetais (FCVC)**    | Inteiro     | A pessoa geralmente come vegetais em suas refeições? (1-3, onde 1 = raramente e 3 = sempre) |
--| **Número de refeições principais (NCP)** | Contínuo    | Quantas refeições principais a pessoa faz por dia?                            |
--| **Consumo de alimentos entre refeições (CAEC)** | Categórico  | A pessoa come alimentos entre as refeições? (Nunca, Às vezes, Frequentemente, Sempre) |
--| **Fuma (SMOKE)**                 | Binário     | A pessoa fuma? (Sim/Não)                                                      |
--| **Consumo de água (CH2O)**       | Contínuo    | Quantos litros de água a pessoa bebe por dia?                                 |
--| **Controle de calorias (SCC)**   | Binário     | A pessoa monitora as calorias que consome diariamente? (Sim/Não)              |
--| **Frequência de atividade física (FAF)** | Contínuo    | Com que frequência a pessoa realiza atividades físicas? (1-3, onde 1 = raramente e 3 = frequentemente) |
--| **Uso de dispositivos tecnológicos (TUE)** | Inteiro     | Quanto tempo a pessoa utiliza dispositivos tecnológicos como celular, videogame, TV, computador e outros? (em horas por dia) |
--| **Frequência de consumo de álcool (CALC)** | Categórico  | Com que frequência a pessoa consome álcool? (Nunca, Às vezes, Frequentemente, Sempre) |
--| **Meio de transporte (MTRANS)**  | Categórico  | Qual meio de transporte a pessoa geralmente utiliza? (A pé, Bicicleta, Transporte público, Carro particular, Moto) |
--| **Nível de Obesidade (NObeyesdad)** | Categórico (Alvo) | Nível de obesidade da pessoa (Peso normal, Sobrepeso, Obesidade tipo I, Obesidade tipo II, etc.) |

-- Relação entre Consumo de alta caloria e Obesidade (Grafico pizza)
SELECT 
    c.favc,
    COUNT(o.id) AS total_obesidade
FROM 
    obesidade o
JOIN 
    compalimentar c ON o.comportamento_alimentar_id = c.id
GROUP BY 
    c.favc;

-- Relação entre consumo de água, frequência de atividade física e obesidade (Barras)
SELECT 
    avg(af.faf) AS frequencia_atividade_fisica_media,
    af.ch2o AS consumo_agua,
    o.nobeyesdad AS nivel_obesidade
FROM 
    obesidade o
JOIN 
    atividade_fisica af ON o.atividade_fisica_id = af.id
GROUP BY 
    af.faf, af.ch2o, o.nobeyesdad







