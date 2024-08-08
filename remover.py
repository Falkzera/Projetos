import os

# Caminho para o arquivo de configuração
zshrc_path = os.path.expanduser('~/.zshrc')

# Ler o conteúdo atual do arquivo
with open(zshrc_path, 'r') as file:
    lines = file.readlines()

# Linhas a serem removidas
lines_to_remove = [
    "PROMPT='%F{blue}%~%f $(git_prompt_info) %F{green}🐍 $(python_version)%f %F{yellow}[%*]%f %# '",
    "python_version() {",
    "  if command -v python3 > /dev/null; then",
    "    echo \"Python $(python3 --version | cut -d \" \" -f 2)\"",
    "  fi",
    "}",
    "git_prompt_info() {",
    "  local branch=$(git symbolic-ref HEAD 2>/dev/null) || return",
    "  branch=${branch##refs/heads/}",
    "  echo \"%F{red}($branch)%f\"",
    "}"
]

# Filtrar linhas que não devem ser removidas
filtered_lines = [line for line in lines if line.strip() not in [line.strip() for line in lines_to_remove]]

# Escrever o conteúdo atualizado no arquivo
with open(zshrc_path, 'w') as file:
    file.writelines(filtered_lines)

print("Arquivo ~/.zshrc atualizado com sucesso.")
