# Projeto Python - Arquitetura DDD

## Estrutura do Projeto

Este projeto segue os princípios de Domain-Driven Design (DDD).

### Camadas

- **Domain**: Regras de negócio puras, independentes de tecnologia
- **Application**: Casos de uso e orquestração
- **Infrastructure**: Implementações técnicas (banco de dados, APIs externas)
- **Presentation**: Interface com o usuário (views, controllers)

### Como Executar

1. Criar ambiente virtual:
```
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Instalar dependências:
```
pip install -r requirements.txt
```

3. Executar aplicação:
```
python main.py
```

## Testes

```
pytest tests/
```
