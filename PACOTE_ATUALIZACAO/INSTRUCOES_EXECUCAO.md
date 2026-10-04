# GUIA DE ATUALIZAÇÃO CIRÚRGICA — 4 LANDING PAGES APLIK DECOR
**Data do Briefing:** 03 de Outubro de 2026 (Briefing WhatsApp Juliana / Pixel)  
**Repositório Alvo:** `C:\Projetos\Pixel\Landing Pages\Aplik Decor`

---

## 📌 REGRA GERAL VÁLIDA PARA TODAS AS 4 LPs
A sequência oficial de produtos e serviços em **TODAS** as páginas (menus, seções de soluções, projetos e rodapé) DEVE ser:
1. **Papel de Parede**
2. **Piso (Piso Vinílico)**
3. **Moldura Boiserie**

---

## 📁 MAPEAMENTO DAS IMAGENS PREPARADAS
Todas as imagens enviadas por Juliana no WhatsApp já foram renomeadas, tratadas e organizadas na pasta `images/novas/`:

### 1. Feedbacks dos Clientes (`images/novas/feedbacks/`)
* `cliente-01-adriano.jpg` -> Adriano Loos (Psicólogo, Primavera do Leste)
* `cliente-02-roberto.jpg` -> Roberto Pelegrini (Pelegrini Representações)
* `cliente-03-edilene.jpg` -> Edilene Souza (Quarto Casal)
* `cliente-04-mirian.jpg` -> Mirian Luciano (Rondonópolis MT)
* `cliente-05-hellen.jpg` -> Hellen Cristina (Lavabo, Poxoréo MT)

### 2. Capas dos Projetos (`images/novas/capas/`) — *Centralizar a foto na exibição (`object-position: center`)*
* `capa-papel-de-parede.jpg` (Capa de Papel de Parede)
* `capa-piso-vinilico.jpg` (Capa de Piso Vinílico)
* `capa-moldura-boiserie.jpg` (Capa de Moldura Boiserie)

### 3. Projetos Reais (`images/novas/projetos/`)
* **Papel de Parede (6 fotos):**
  * `papel-01-ripado-marmorizado.jpg`
  * `papel-02-quarto-menina.jpg`
  * `papel-03-tradicional-ripado.jpg`
  * `papel-04-tradicional-linho.jpg`
  * `papel-05-papel-liquido.jpg`
  * `papel-06-estampado-lavabo.jpg`
* **Piso Vinílico (3 fotos):**
  * `piso-01-ambiente-instalado.jpg`
  * `piso-02-mostruario-padroes.jpg`
  * `piso-03-living-amadeirado.jpg`
* **Molduras Boiserie (6 fotos):**
  * `boiserie-01-painel-geometrico.jpg`
  * `boiserie-02-com-papel-liquido.jpg`
  * `boiserie-03-personalizado-luxo.jpg`
  * `boiserie-04-classico-sala.jpg`
  * `boiserie-05-com-ripado.jpg`
  * `boiserie-06-quarto-bebe.jpg`

---

## 🛠️ ALTERAÇÕES ESPECÍFICAS POR ARQUIVO

### 1. `index.html` (Landing Page Principal)

#### A. Seção Soluções (`#solucoes`)
* **Antes:** 1. Piso Vinílico, 2. Moldura Boiserie, 3. Papel de Parede.
* **Depois:** Reordenar os cards para:
  1. Card de **Papel de Parede**
  2. Card de **Piso Vinílico**
  3. Card de **Moldura Boiserie**

#### B. Seção Quem Somos (`#quem-somos`)
* **Texto de História:** Substituir pela cópia oficial de Juliana:
  > Somos a **Aplikdecor**, uma empresa que está no mercado há mais de 12 anos. Tudo começou com uma oportunidade de emprego e foi onde as portas se abriram de um simples funcionário que se dedicou, aprendeu cada detalhe e se tornou instalador profissional de papel de parede. Com dedicação, determinação incansável e paixão pelo acabamento impecável, essa jornada evoluiu de instalador a empresário consolidado, vendendo papéis de parede e expandindo para outros nichos que agregam sofisticação ao ramo. Somos hoje especialistas em transformar ambientes através da decoração e dos revestimentos de alto padrão.
  >
  > *"Mais do que vender produtos, nosso objetivo é entender o que cada cliente deseja e ajudar a transformar sua ideia em um ambiente bonito, aconchegante e personalizado. Acreditamos que cada detalhe faz a diferença, e é por isso que cuidamos de cada projeto com profissionalismo, capricho e compromisso."*
  >
  > Trabalhamos com papel de parede tradicional, papel de parede líquido, pedras naturais, piso vinílico, molduras boiserie e outros produtos decorativos. Mais que estética: durabilidade, precisão e excelência em cada acabamento.
* **Selo de Destaque:**
  * Alterar texto para: **"12+ ANOS TRANSFORMANDO AMBIENTES COM EXCELÊNCIA"**

#### C. Seção de Projetos (`#projetos`)
* Estruturar a galeria respeitando a sequência e quantidade solicitadas:
  1. **Papel de Parede:** 6 fotos (Capa: `images/novas/capas/capa-papel-de-parede.jpg`, centralizada)
  2. **Piso Vinílico:** 3 fotos (Capa: `images/novas/capas/capa-piso-vinilico.jpg`, centralizada)
  3. **Moldura Boiserie:** 6 fotos (Capa: `images/novas/capas/capa-moldura-boiserie.jpg`, centralizada)

#### D. Seção Diferenciais (`#por-que`)
* **Título dos Diferenciais em Caixa Alta e Aumentar Fonte:**
  * De "Atendimento Consultivo" para: **ATENDIMENTO PERSONALIZADO**
  * De "Qualidade Comprovada" para: **QUALIDADE COMPROVADA**
  * De "Solução Completa" para: **SOLUÇÃO COMPLETA**
  * De "Acabamento Premium" para: **ACABAMENTO PREMIUM**
* **Texto do Acabamento Premium:**
  * Alterar para: *"Valorizamos cada detalhe, porque acreditamos que a excelência está no resultado final."*
* Remover quebras de linha (`<br>`) nos parágrafos dos diferenciais para manter texto contínuo padronizado.

#### E. Seção de Depoimentos (`#depoimentos`)
* Atualizar para os 5 depoimentos completos com as fotos em `images/novas/feedbacks/`:
  1. **Adriano Loos** — Psicólogo (Consultório em Primavera do Leste) | `cliente-01-adriano.jpg`  
     *"Passando para agradecer pelo trabalho desempenhado aqui no meu consultório pelo Welber papel de parede com aplicação incrível, trouxe aqui uma sensação de leveza e bem-estar. Muito obrigado pelo profissionalismo, está recomendado"*
  2. **Roberto Pelegrini** — Pelegrini Representações (Primavera do Leste) | `cliente-02-roberto.jpg`  
     *"Uelber muito obrigado, o papel ripado ficou excelente, com certeza faremos novamente em outros ambientes! A Vania adorou, ficou encantada."*
  3. **Edilene Souza** — Quarto casal (Primavera do Leste) | `cliente-03-edilene.jpg`  
     *"Uelber passando aqui pra dizer que amei o papel de parede líquido superou minha expectativa rsrs, ficou muito boa a parede !!"*
  4. **Mirian Luciano** — Rondonópolis MT | `cliente-04-mirian.jpg`  
     *"Essa empresa é super recomendada, aqui em Rondonópolis eles prestam um serviço de excelência. Já faço serviço com eles há mais de 8 anos, sempre com qualidade, cumprimento de prazo e ótimos preços. Nossa parceria continua e em breve faremos novos projetos. Grata!"*
  5. **Hellen Cristina** — Lavabo (Poxoréo MT) | `cliente-05-hellen.jpg`  
     *"Só pra deixar registrado que meu lavabo ficou chique demais e o papel de parede linho realmente valorizou e ficou perfeito. Muito obrigado ao profissionalismo !!"*

#### F. Seção CTA Final (`.cta-final`)
* Título: Manter *"Seu projeto começa com uma boa escolha."* sem quebra de linha.
* Subtítulo: Manter *"Mato Grosso e região"* na mesma linha.
* Botão em caixa alta: **"QUERO ENCONTRAR A MINHA SOLUÇÃO"**.

#### G. Seção FAQ (`#faq`)
* Título em Amarelo e Caixa Alta: `<h2 class="section-title text-yellow" style="color: #e5a93c;">PERGUNTAS FREQUENTES</h2>`
* Perguntas e Respostas:
  * **P1:** *Quais produtos Aplikdecor oferece?*  
    **R:** Trabalhamos com uma linha completa de soluções para transformar e valorizar seu ambiente, incluindo papéis de parede em diversos modelos, estilos e texturas, papel de parede líquido com várias opções de cores, piso vinílico disponível em diferentes cores, e molduras boiserie para um acabamento sofisticado e personalizado.
  * **P2:** *Vocês realizam a instalação?*  
    **R:** Sim, para papel de parede, piso vinílico e molduras a instalação profissional já é inclusa.
  * **P3:** *Quais cidades e regiões atendem?*  
    **R:** Nossa base é em Primavera do Leste MT. Mas atendemos também Campo Verde, Poxoréu, Rondonópolis, Paranatinga e outras cidades da região.

#### H. Rodapé (`footer`)
* Descrição da empresa: *"Especialista em transformação de ambientes há mais de 12 anos em Primavera do Leste."*
* Aumentar fonte dos títulos e itens.
* Sequência da coluna Produtos:
  1. Papel de parede
  2. Papel de parede líquido
  3. Pedras naturais
  4. Piso vinílico
  5. Projetos
* Coluna Localização:
  * Endereço: *Rua Rafael Borgetti, Nº 110, Bairro Castelândia - Primavera do Leste MT / CEP: 78.850-000*
  * Telefone / Contato: *(66) 99670-6972*

---

### 2. `papel-de-parede.html` (LP Específica de Papel de Parede)
* **Navegação (Header):** Manter sequência oficial de links (Papel de Parede, Piso Vinílico, Moldura Boiserie).
* **Galeria de Projetos:** Exibir as 6 fotos oficiais de papel de parede de `images/novas/projetos/papel-de-parede/` com a Capa `images/novas/capas/capa-papel-de-parede.jpg`.
* **Rodapé:** Atualizar com os mesmos dados padronizados (endereço completo, telefone (66) 99670-6972 e lista de produtos na sequência oficial).

---

### 3. `piso-vinilico.html` (LP Específica de Piso Vinílico)
* **Navegação (Header):** Manter sequência oficial de links.
* **Galeria de Projetos:** Exibir as 3 fotos oficiais de piso vinílico de `images/novas/projetos/piso-vinilico/` com a Capa `images/novas/capas/capa-piso-vinilico.jpg`.
* **Rodapé:** Atualizar com os dados padronizados.

---

### 4. `boiserie.html` (LP Específica de Moldura Boiserie)
* **Navegação (Header):** Manter sequência oficial de links.
* **Galeria de Projetos:** Exibir as 6 fotos oficiais de boiserie de `images/novas/projetos/boiserie/` com a Capa `images/novas/capas/capa-moldura-boiserie.jpg`.
* **Rodapé:** Atualizar com os dados padronizados.

---

### 5. `style.css`
* Adicionar suporte a cores e alinhamento:
  ```css
  /* FAQ Amarelo e Caixa Alta */
  #faq .section-title {
    color: #e5a93c !important;
    text-transform: uppercase !important;
  }

  /* Centralização das Capas de Projetos */
  .capa-centralizada, .gitem-capa img {
    object-position: center center !important;
    object-fit: cover !important;
  }

  /* Aumento de fonte do Rodapé e Diferenciais */
  .why-item h3 {
    font-size: 1.15rem;
    letter-spacing: 0.5px;
  }
  .footer-col h4 {
    font-size: 1.1rem;
  }
  .footer-links a, .footer-contact p {
    font-size: 0.95rem;
  }
  ```

---

## ⚡ EXECUÇÃO AUTOMATIZADA (OPCIONAL)
Caso prefira aplicar tudo de forma 100% automatizada e validada em segundos, basta executar no terminal dentro da pasta do repositório:
```bash
python PACOTE_ATUALIZACAO/aplicar_atualizacao.py
```
