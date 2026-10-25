# Playwright setup with Python and CI

## Resumo e finalidade do projeto

Este projeto automatiza testes de navegador para o aplicativo de exemplo disponível em `https://erickwendel.github.io/vanilla-js-web-app-example/`. Ele não implementa nem hospeda o aplicativo: sua finalidade é verificar, de forma repetível, se os principais comportamentos da página continuam funcionando.

Os testes simulam o uso do formulário de imagens e verificam se uma imagem enviada aparece na lista, se o sistema apresenta mensagens quando os campos obrigatórios estão vazios e se rejeita uma URL inválida. Para isso, o projeto usa Python, pytest e Playwright, executando os testes no navegador Chromium.

O workflow do GitHub Actions executa essa validação automaticamente em alterações enviadas ao repositório e em pull requests. Assim, problemas podem ser identificados antes de integrar mudanças, e um relatório HTML fica disponível como artefato quando a execução falha.

## Goal

Test the app at `https://erickwendel.github.io/vanilla-js-web-app-example/`.

## What to include

- Use Python, Playwright, and pytest.
- Configure the base URL and a timeout no greater than 5 seconds.
- Add tests for form submission/list updates and form validation.
- Run Chromium only in GitHub Actions.
- Generate an HTML report in CI and upload it when tests fail.

## Local setup

1. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install the test dependencies:

   ```powershell
   py -m pip install -r requirements.txt
   ```

3. Install only Chromium:

   ```powershell
   py -m playwright install chromium
   ```

4. Run the tests:

   ```powershell
   py -m pytest
   ```

The tests use Playwright's synchronous Python API and the `page` fixture from `pytest-playwright`. `pytest-html` generates the CI report.

## Configuration

`pytest.ini` sets the app URL as `base_url` and sets Playwright's default action/navigation timeout to 5000 ms. Tests use Chromium in headless mode locally and in CI.

## GitHub Actions

The workflow in `.github/workflows/playwright.yml` sets up Python, installs dependencies from `requirements.txt`, installs Chromium with its Linux system dependencies, and runs pytest. It uploads `report.html` on failure.

## O que cada arquivo faz

- `project-scaffolding.md`: documenta o objetivo, a configuração, os comandos para executar os testes localmente e o funcionamento do CI.
- `requirements.txt`: lista as dependências Python do projeto: `pytest` para executar os testes, `pytest-playwright` para integrar o Playwright ao pytest e `pytest-html` para gerar o relatório HTML.
- `pytest.ini`: configura o pytest para usar Chromium e define a URL do aplicativo como endereço base (`base_url`) para os testes.
- `conftest.py`: configura, para cada teste, os timeouts padrão de ações e navegação do Playwright em 5 segundos.
- `tests/test_image_form.py`: contém os testes automatizados de envio do formulário, atualização da lista e validação dos campos.
- `.github/workflows/playwright.yml`: define a automação do GitHub Actions. Ela instala Python, as dependências e Chromium, executa os testes e publica o relatório HTML como artefato se a execução falhar.
- `.gitignore`: evita que o ambiente virtual, caches do Python/pytest e o relatório gerado sejam incluídos no controle de versão.
- `generate-tests.md`: descreve o cenário e os comportamentos do aplicativo para os quais devem ser criados testes.
- `generate_test.prompt.md`: contém as instruções para gerar testes Python com Playwright, incluindo como observar a página, escolher seletores acessíveis e executar os testes.
- `links.txt`: guarda a URL do aplicativo testado.

O diretório `.github/workflows/` contém o workflow do CI, e `tests/` reúne os arquivos de teste. `.venv/` é criado localmente pelo comando `py -m venv .venv` e contém o ambiente virtual Python; não é um arquivo do projeto nem deve ser versionado.
