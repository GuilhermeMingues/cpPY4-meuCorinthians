const jogadoresElenco = [
    // Goleiros
    {nome: "Hugo Souza", numero: 1, posicao: "Goleiro"},
    {nome: "Felipe Longo", numero: 40, posicao: "Goleiro"},
    {nome: "Kauê", numero: 51, posicao: "Goleiro"},

    // Zagueiros
    {nome: "Gabriel Paulista", numero: 3, posicao: "Zagueiro"},
    {nome: "João Pedro", numero: 4, posicao: "Zagueiro"},
    {nome: "André Ramalho", numero: 5, posicao: "Zagueiro"},
    {nome: "Gustavo Henrique", numero: 13, posicao: "Zagueiro"},

    // Laterais
    {nome: "Matheuzinho", numero: 2, posicao: "Lateral-direito"},
    {nome: "Pedro Milans", numero: 20, posicao: "Lateral-direito"},
    {nome: "João Vitor", numero: 59, posicao: "Lateral-direito"},
    {nome: "Matheus Bidu", numero: 21, posicao: "Lateral-esquerdo"},
    {nome: "Fabrizio Angileri", numero: 26, posicao: "Lateral-esquerdo"},
    {nome: "Hugo Ferreira", numero: 46, posicao: "Lateral-esquerdo"},

    // Volantes
    {nome: "Raniele", numero: 14, posicao: "Volante"},
    {nome: "Matheus Pereira", numero: 23, posicao: "Volante"},
    {nome: "Allan", numero: 29, posicao: "Volante"},
    {nome: "Charles", numero: 35, posicao: "Volante"},
    {nome: "André", numero: 49, posicao: "Volante"},
    {nome: "Luiz Gustavo", numero: 54, posicao: "Volante"},
    {nome: "Alex Santana", numero: 80, posicao: "Volante"},

    // Meias
    {nome: "Breno Bidon", numero: 7, posicao: "Meia"},
    {nome: "Rodrigo Garro", numero: 8, posicao: "Meia"},
    {nome: "André Carrillo", numero: 19, posicao: "Meia"},
    {nome: "Gui Amorim", numero: 48, posicao: "Meia"},
    {nome: "Zakaria Labyad", numero: 52, posicao: "Meia"},

    // Atacantes
    {nome: "Yuri Alberto", numero: 9, posicao: "Atacante"},
    {nome: "Memphis Depay", numero: 10, posicao: "Atacante"},
    {nome: "Vitinho", numero: 11, posicao: "Atacante"},
    {nome: "Pedro Raul", numero: 18, posicao: "Atacante"},
    {nome: "Kayke", numero: 31, posicao: "Atacante"},
    {nome: "Kaio César", numero: 37, posicao: "Atacante"},
    {nome: "Gui Negão", numero: 56, posicao: "Atacante"},
    {nome: "Dieguinho", numero: 61, posicao: "Atacante"},
    {nome: "Jesse Lingard", numero: 77, posicao: "Atacante"}
];

const containerElenco = document.getElementById("elenco-lista");
console.log(containerElenco);

const gruposElenco = [
  { chave: "Goleiro", titulo: "GOLEIROS" },
  { chave: "Zagueiro", titulo: "ZAGUEIROS" },
  { chave: "Lateral-direito", titulo: "LATERAIS-DIREITOS" },
  { chave: "Lateral-esquerdo", titulo: "LATERAIS-ESQUERDOS" },
  { chave: "Volante", titulo: "VOLANTES" },
  { chave: "Meia", titulo: "MEIAS" },
  { chave: "Atacante", titulo: "ATACANTES" },
];

function criarCardHTML(jogador) {
  return `
    <article class="card-elenco">
      <div class="card-elenco__topo">
        <span class="card-elenco__numero">${String(jogador.numero).padStart(2, "0")}</span>
        <button class="favorito" type="button" aria-label="Favoritar jogador">
          ☆
        </button>
      </div>

      <div class="card-elenco__info">
        <h3>${jogador.nome}</h3>
        <span>${jogador.posicao}</span>
      </div>
    </article>
  `;
}
containerElenco.addEventListener("click", (evento) => {
  const botaoFavorito = evento.target.closest(".favorito");
  if (!botaoFavorito) return; // clicou em outra parte do card, não faz nada

  const jaFavoritado = botaoFavorito.classList.toggle("favorito--ativo");
  botaoFavorito.textContent = jaFavoritado ? "★" : "☆";
});

function criarGrupoHTML(grupo) {
  const jogadoresDoGrupo = jogadoresElenco.filter(j => j.posicao === grupo.chave);

  if (jogadoresDoGrupo.length === 0) return "";

  const cardsHTML = jogadoresDoGrupo.map(criarCardHTML).join("");

  return `
    <h4 class="elenco-grupo-titulo">${grupo.titulo}</h4>
    <div class="cards-elenco">
      ${cardsHTML}
    </div>
  `;
}


const botoesScroll = document.querySelectorAll("[data-scroll-to]");

botoesScroll.forEach(botao => {
  botao.addEventListener("click", () => {
    const alvoSeletor = botao.dataset.scrollTo;
    const alvoElemento = document.querySelector(alvoSeletor);
    alvoElemento.scrollIntoView({ behavior: "smooth" });
  });
});

containerElenco.innerHTML = gruposElenco.map(criarGrupoHTML).join("");