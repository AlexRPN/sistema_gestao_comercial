param(
    [Parameter(Mandatory = $false)]
    [string]$ProjectPath = "."
)

# Navegar para o diretório do projeto
Set-Location $ProjectPath

Write-Host "🚀 Criando estrutura DDD em: $ProjectPath" -ForegroundColor Cyan

# Definir todas as pastas da estrutura DDD
$folders = @(
    "src/domain/entities",
    "src/domain/value_objects",
    "src/domain/repositories",
    "src/domain/services",
    "src/domain/exceptions",
    "src/application/use_cases",
    "src/application/dtos",
    "src/application/services",
    "src/infrastructure/database/migrations",
    "src/infrastructure/repositories",
    "src/infrastructure/config",
    "src/infrastructure/external_services",
    "src/presentation/views",
    "src/presentation/controllers",
    "src/presentation/components",
    "src/presentation/styles",
    "tests/unit/domain",
    "tests/unit/application",
    "tests/unit/infrastructure",
    "tests/integration",
    "docs"
)

# Criar pastas e arquivos __init__.py
Write-Host "📁 Criando estrutura de pastas..." -ForegroundColor Yellow
foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path $folder | Out-Null
    New-Item -ItemType File -Force -Path "$folder/__init__.py" | Out-Null
}

# Criar arquivos na raiz
Write-Host "📄 Criando arquivos raiz..." -ForegroundColor Yellow
New-Item -ItemType File -Force -Path "main.py" | Out-Null
New-Item -ItemType File -Force -Path "requirements.txt" | Out-Null
New-Item -ItemType File -Force -Path ".env" | Out-Null
New-Item -ItemType File -Force -Path "README.md" | Out-Null

# Criar .gitignore com conteúdo básico
$gitignoreContent = @"
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Environment variables
.env
.env.local

# Database
*.db
*.sqlite3

# OS
.DS_Store
Thumbs.db
"@

Set-Content -Path ".gitignore" -Value $gitignoreContent

# Criar README.md básico
$readmeContent = @"
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
``````
python -m venv venv
venv\Scripts\Activate.ps1
``````

2. Instalar dependências:
``````
pip install -r requirements.txt
``````

3. Executar aplicação:
``````
python main.py
``````

## Testes

``````
pytest tests/
``````
"@

Set-Content -Path "README.md" -Value $readmeContent

Write-Host "`n✅ Estrutura DDD criada com sucesso!" -ForegroundColor Green
Write-Host "`n📊 Resumo:" -ForegroundColor Cyan
Write-Host "   - $($folders.Count) diretórios criados" -ForegroundColor White
Write-Host "   - Arquivos __init__.py em todas as pastas" -ForegroundColor White
Write-Host "   - Arquivos raiz: main.py, requirements.txt, .env, .gitignore, README.md" -ForegroundColor White
Write-Host "`n💡 Próximos passos:" -ForegroundColor Cyan
Write-Host "   1. python -m venv venv" -ForegroundColor White
Write-Host "   2. venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "   3. Começar a desenvolver! 🚀" -ForegroundColor White
