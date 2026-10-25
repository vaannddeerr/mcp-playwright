# Configurar o Playwright MCP no VS Code

Este guia mostra como instalar e usar o servidor **Playwright MCP oficial da Microsoft** no VS Code.

> **Importante:** o MCP normalmente abre um navegador próprio controlado pelo Playwright. Ele não controla automaticamente uma janela já aberta do Chrome nem a sessão do navegador integrado do VS Code; são formas diferentes de automação.

## Atalhos úteis no VS Code (Windows)

| Ação | Atalho |
| --- | --- |
| Abrir a Paleta de Comandos | `Ctrl+Shift+P` |
| Abrir ou fechar o terminal integrado | `` Ctrl+` `` |
| Abrir a visualização de Extensões | `Ctrl+Shift+X` |
| Abrir o Chat do Copilot | `Ctrl+Alt+I` |

Também é possível acessar essas opções pelos menus **Exibir** (Paleta de Comandos e Terminal) e **Extensões**. No macOS, a tecla `Ctrl` costuma ser substituída por `Cmd` nos atalhos do VS Code.

Para executar qualquer comando da Paleta, pressione `Ctrl+Shift+P`, digite o nome do comando e pressione `Enter`. Por exemplo: `MCP: Add Server`.

## 1. Instale o Node.js

O servidor MCP é iniciado pelo `npx`, que vem com o Node.js. No Windows, abra o terminal do VS Code e confira:

```powershell
# Abra com Ctrl+` ou pelo menu Terminal > Novo Terminal
node --version
npx --version
```

Se os comandos não forem reconhecidos, instale a versão LTS do [Node.js](https://nodejs.org/) e reinicie o VS Code. O Playwright MCP requer Node.js 18 ou superior.

## 2. Adicione o MCP ao VS Code

1. Abra a paleta de comandos com **Ctrl+Shift+P**.
2. Execute **MCP: Add Server**.
3. Selecione **Command (stdio)**.
4. Informe o comando:

   ```text
   npx -y @playwright/mcp@latest
   ```

5. Dê um identificador, por exemplo, `playwright`.
6. Escolha **Global** e depois **Copilot Global** para usar em diferentes projetos, ou selecione uma configuração de workspace para limitar o servidor ao projeto.
7. Revise os avisos de confiança apresentados pelo VS Code antes de aceitá-los.

Não é necessário instalar uma extensão do Playwright para esse servidor. O VS Code inicia o pacote MCP com o `npx`.

### Alternativa: instalar pelo terminal do VS Code

Se o comando `code` estiver disponível no PATH, abra o terminal integrado com `` Ctrl+` `` e execute:

```powershell
code --add-mcp '{"name":"playwright","command":"npx","args":["@playwright/mcp@latest"]}'
```

Depois, reinicie ou atualize o servidor MCP no VS Code. Se `code` não for reconhecido, use o fluxo pela Paleta de Comandos acima ou configure o PATH do VS Code.

### Alternativa: configurar por arquivo

Você também pode criar ou editar `.vscode/mcp.json` no projeto:

```json
{
  "servers": {
    "playwright": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

O VS Code pode oferecer outra localização de configuração durante o fluxo guiado. Para uso pessoal, a configuração **Copilot Global** evita adicionar o MCP ao projeto.

## 3. Inicie e verifique o servidor

Depois de salvar a configuração:

1. Pressione `Ctrl+Shift+P`.
2. Digite e execute **MCP: List Servers** para localizar o servidor.
3. Se ele não estiver ativo, use as ações de iniciar ou reiniciar disponíveis para `playwright`.
4. Abra o Chat do Copilot com `Ctrl+Alt+I` e envie o teste abaixo.

Em uma conversa do Copilot, faça um teste sem efeitos colaterais:

> Use o servidor MCP Playwright para abrir `https://example.com` e informar o título da página. Não clique em links nem altere nada.

A conexão está verificada quando o Copilot chama uma ferramenta do servidor Playwright e retorna o título com base no resultado — não apenas por dizer que o servidor está configurado.

## 4. Use-o para interagir com páginas

Depois do teste, você pode pedir tarefas como:

> Use o Playwright MCP para abrir [site], analisar os campos disponíveis e me dizer o que precisa ser preenchido antes de continuar.

Para tarefas de preenchimento, é boa prática separar a ação da confirmação final:

> Preencha os campos com estes dados e confira se estão corretos. **Não envie o formulário** até eu confirmar.

Antes de enviar, publicar, comprar ou excluir algo, revise o conteúdo e confirme a ação final.

## Sessões autenticadas e dados sensíveis

Se o site exigir login, autentique-se no navegador aberto pelo MCP, se ele permitir interação manual. A sessão desse navegador pode ser diferente da sessão do seu Chrome habitual.

O Playwright MCP pode ser configurado com um perfil de navegador dedicado e persistente, mas esse perfil contém cookies e dados de sessão. Mantenha-o privado e não o coloque no Git. Evite compartilhar senhas ou tokens no chat.

## Referências oficiais

- [Playwright MCP da Microsoft](https://github.com/microsoft/playwright-mcp)
- [Adicionar servidores MCP no VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)
- [Documentação do Playwright](https://playwright.dev/docs/intro)

> **Nota:** o VS Code também oferece ferramentas de navegador integradas. Elas podem ser mais convenientes para interagir com páginas já abertas no ambiente do VS Code; `@playwright/mcp` é uma alternativa para configurar um servidor MCP próprio.
