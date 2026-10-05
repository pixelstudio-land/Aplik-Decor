# -*- coding: utf-8 -*-
"""
Script de aplicação automatizada e cirúrgica das alterações de Outubro/2026
nas 4 Landing Pages da Aplik Decor conforme o briefing da Juliana (03/10/2026).
"""

import os
import re

def atualizar_style_css(repo_dir):
    p_css = os.path.join(repo_dir, "style.css")
    if not os.path.exists(p_css):
        print("style.css não encontrado!")
        return

    with open(p_css, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    custom_css = """
/* ==============================================================================
   AJUSTES OUTUBRO 2026 - BRIEFING JULIANA
   ============================================================================== */
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

/* Aumento de fonte dos Diferenciais */
.why-card h3, .why-item h3, .why-title {
  font-size: 1.15rem !important;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

/* Aumento de fonte do Rodapé */
.footer-col h4, .footer-title {
  font-size: 1.1rem !important;
}

.footer-links a, .footer-contact p, .footer-contact span, .footer-contact-item span, .footer-contact-item p {
  font-size: 0.95rem !important;
}

/* Ajuste responsivo dos Depoimentos (5 cards) */
@media (min-width: 992px) {
  .testimonials-grid {
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  }
}
"""
    if "AJUSTES OUTUBRO 2026" not in content:
        content = content.rstrip() + "\n" + custom_css + "\n"
        with open(p_css, "w", encoding="utf-8", newline="\r\n") as f:
            f.write(content)
        print("[OK] style.css atualizado com sucesso!")
    else:
        print("[OK] style.css ja continha os ajustes de Outubro 2026.")


def atualizar_index_html(repo_dir):
    p_index = os.path.join(repo_dir, "index.html")
    if not os.path.exists(p_index):
        print("index.html não encontrado!")
        return

    with open(p_index, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()

    # 1. Header Menu (ordem oficial: Produtos, Quem Somos, Projetos...)
    # 2. Soluções: Sequência Papel de Parede, Piso Vinílico, Moldura Boiserie com as Capas centralizadas
    solucoes_novo = """    <div class="product-cards">
      <!-- Papel de Parede -->
      <article class="product-card" data-anim data-delay="1">
        <div class="product-card-img">
          <img src="images/novas/capas/capa-papel-de-parede.jpg" alt="Papel de parede instalado pela Aplik Decor" class="capa-centralizada" loading="lazy">
        </div>
        <div class="product-card-body">
          <div class="product-card-tag">Papel de Parede</div>
          <h3 class="product-card-title">Mais de 400 padrões e texturas para transformar qualquer cômodo.</h3>
          <p class="product-card-desc">Linho, ripado, cimento queimado, marmorizado, infantil e laváveis com 12 anos de especialidade.</p>
          <div class="product-card-price">A partir de R$ 449 o rolo c/ instalação</div>
          <a href="papel-de-parede.html" class="btn btn-gold" data-cta="papel">
            Conhecer Papel de Parede
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
          </a>
        </div>
      </article>

      <!-- Piso Vinílico -->
      <article class="product-card" data-anim data-delay="2">
        <div class="product-card-img">
          <img src="images/novas/capas/capa-piso-vinilico.jpg" alt="Piso vinílico instalado pela Aplik Decor" class="capa-centralizada" loading="lazy">
        </div>
        <div class="product-card-body">
          <div class="product-card-tag">Piso Vinílico</div>
          <h3 class="product-card-title">Conforto térmico, acústico e sofisticação sem precisar de reforma.</h3>
          <p class="product-card-desc">Acabamento moderno que valoriza qualquer cômodo. Instalação rápida diretamente sobre o piso atual.</p>
          <div class="product-card-price">A partir de R$ 219/m² já aplicado</div>
          <a href="piso-vinilico.html" class="btn btn-gold" data-cta="piso">
            Conhecer Piso Vinílico
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
          </a>
        </div>
      </article>

      <!-- Moldura Boiserie -->
      <article class="product-card" data-anim data-delay="3">
        <div class="product-card-img">
          <img src="images/novas/capas/capa-moldura-boiserie.jpg" alt="Parede com moldura Boiserie instalada pela Aplik Decor" class="capa-centralizada" loading="lazy">
        </div>
        <div class="product-card-body">
          <div class="product-card-tag">Moldura Boiserie</div>
          <h3 class="product-card-title">Acabamento arquitetônico elegante para dar identidade às paredes.</h3>
          <p class="product-card-desc">Painéis clássicos e contemporâneos sob medida. Do projeto à instalação e acabamento.</p>
          <div class="product-card-price">A partir de R$ 49,99/m linear</div>
          <a href="boiserie.html" class="btn btn-gold" data-cta="boiserie">
            Conhecer Boiserie
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
          </a>
        </div>
      </article>
    </div>"""

    c = re.sub(
        r'<div class="product-cards">.*?</div>\s*</div>\s*</section>',
        solucoes_novo + "\n  </div>\n</section>",
        c,
        flags=re.DOTALL
    )

    # 3. Quem Somos: Selo de Destaque
    selo_novo = """        <div class="about-experience-badge">
          <div class="about-exp-num">12+</div>
          <div class="about-exp-text">
            12+ ANOS TRANSFORMANDO<br>AMBIENTES COM EXCELÊNCIA
          </div>
        </div>"""
    c = re.sub(
        r'<div class="about-experience-badge">.*?</div>\s*</div>\s*<!-- Texto Institucional',
        selo_novo + "\n      </div>\n\n      <!-- Texto Institucional",
        c,
        flags=re.DOTALL
    )

    # 4. Quem Somos: Texto Oficial de Juliana
    historia_nova = """        <p class="about-intro-p">
          Somos a <strong>Aplikdecor</strong>, uma empresa que está no mercado há mais de 12 anos. Tudo começou com uma oportunidade de emprego e foi onde as portas se abriram de um simples funcionário que se dedicou, aprendeu cada detalhe e se tornou instalador profissional de papel de parede.
        </p>

        <p class="about-desc-p">
          Com dedicação, determinação incansável e paixão pelo acabamento impecável, essa jornada evoluiu de instalador a empresário consolidado, vendendo papéis de parede e expandindo para outros nichos que agregam sofisticação ao ramo. Somos hoje especialistas em transformar ambientes através da decoração e dos revestimentos de alto padrão.
        </p>

        <div class="about-highlight-box">
          "Mais do que vender produtos, nosso objetivo é entender o que cada cliente deseja e ajudar a transformar sua ideia em um ambiente bonito, aconchegante e personalizado. Acreditamos que cada detalhe faz a diferença, e é por isso que cuidamos de cada projeto com profissionalismo, capricho e compromisso."
        </div>

        <p class="about-desc-p">
          Trabalhamos com papel de parede tradicional, papel de parede líquido, pedras naturais, piso vinílico, molduras boiserie e outros produtos decorativos. Mais que estética: durabilidade, precisão e excelência em cada acabamento.
        </p>"""

    c = re.sub(
        r'<p class="about-intro-p">.*?</p>\s*</div>\s*</div>\s*<!-- Cards de Missão',
        historia_nova + "\n      </div>\n\n    </div>\n\n    <!-- Cards de Missão",
        c,
        flags=re.DOTALL
    )

    # 5. Seção de Projetos: Sequência 1. Papel de Parede (6), 2. Piso Vinílico (3), 3. Moldura Boiserie (6)
    projetos_novo = """    <div class="filter-nav" data-anim data-delay="2">
      <button class="filter-btn active" data-filter="all">Todos os Projetos (15)</button>
      <button class="filter-btn" data-filter="papel">Papel de Parede (6)</button>
      <button class="filter-btn" data-filter="piso">Piso Vinílico (3)</button>
      <button class="filter-btn" data-filter="boiserie">Moldura Boiserie (6)</button>
    </div>

    <div class="gallery gallery-3" data-anim>
      <!-- 1. PAPEL DE PAREDE (6 FOTOS) -->
      <div class="gitem ar-43 zoomable style-item" data-category="papel">
        <img src="images/novas/projetos/papel-de-parede/papel-01-ripado-marmorizado.jpg" alt="Papel de parede ripado e marmorizado aplicado pela Aplik Decor" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Papel de Parede • Ripado e Marmorizado</div>
      </div>
      <div class="gitem ar-43 zoomable style-item" data-category="papel">
        <img src="images/novas/projetos/papel-de-parede/papel-02-quarto-menina.jpg" alt="Papel de parede quarto de menina instalado pela Aplik Decor" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Papel de Parede • Quarto de Menina</div>
      </div>
      <div class="gitem ar-43 zoomable style-item" data-category="papel">
        <img src="images/novas/projetos/papel-de-parede/papel-03-tradicional-ripado.jpg" alt="Papel de parede tradicional ripado aplicado pela Aplik Decor" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Papel de Parede • Tradicional Ripado Nobre</div>
      </div>
      <div class="gitem ar-43 zoomable style-item" data-category="papel">
        <img src="images/novas/projetos/papel-de-parede/papel-04-tradicional-linho.jpg" alt="Papel de parede textura linho instalado pela Aplik Decor" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Papel de Parede • Tradicional Linho</div>
      </div>
      <div class="gitem ar-43 zoomable style-item" data-category="papel">
        <img src="images/novas/projetos/papel-de-parede/papel-05-papel-liquido.jpg" alt="Papel de parede líquido aplicado pela Aplik Decor" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Papel de Parede • Textura Papel Líquido</div>
      </div>
      <div class="gitem ar-43 zoomable style-item" data-category="papel">
        <img src="images/novas/projetos/papel-de-parede/papel-06-estampado-lavabo.jpg" alt="Papel de parede estampado para lavabo aplicado pela Aplik Decor" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Papel de Parede • Estampado Exclusivo Lavabo</div>
      </div>

      <!-- 2. PISO VINÍLICO (3 FOTOS) -->
      <div class="gitem ar-43 zoomable style-item" data-category="piso">
        <img src="images/novas/projetos/piso-vinilico/piso-01-ambiente-instalado.jpg" alt="Piso vinílico instalado pela Aplik Decor em ambiente integrado" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Piso Vinílico • Sala & Ambientes Integrados</div>
      </div>
      <div class="gitem ar-43 zoomable style-item" data-category="piso">
        <img src="images/novas/projetos/piso-vinilico/piso-02-mostruario-padroes.jpg" alt="Padrões e texturas de piso vinílico da Aplik Decor" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Piso Vinílico • Mostruário de Padrões e Cores</div>
      </div>
      <div class="gitem ar-43 zoomable style-item" data-category="piso">
        <img src="images/novas/projetos/piso-vinilico/piso-03-living-amadeirado.jpg" alt="Piso vinílico living amadeirado de alto padrão instalado" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Piso Vinílico • Living Amadeirado</div>
      </div>

      <!-- 3. MOLDURAS BOISERIE (6 FOTOS) -->
      <div class="gitem ar-43 zoomable style-item" data-category="boiserie">
        <img src="images/novas/projetos/boiserie/boiserie-01-painel-geometrico.jpg" alt="Moldura boiserie painel geométrico instalado pela Aplik Decor" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Moldura Boiserie • Painel Geométrico</div>
      </div>
      <div class="gitem ar-43 zoomable style-item" data-category="boiserie">
        <img src="images/novas/projetos/boiserie/boiserie-02-com-papel-liquido.jpg" alt="Moldura boiserie combinada com papel líquido" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Moldura Boiserie • Boiserie com Papel Líquido</div>
      </div>
      <div class="gitem ar-43 zoomable style-item" data-category="boiserie">
        <img src="images/novas/projetos/boiserie/boiserie-03-personalizado-luxo.jpg" alt="Moldura boiserie em painel de luxo personalizado" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Moldura Boiserie • Painel de Alto Padrão</div>
      </div>
      <div class="gitem ar-43 zoomable style-item" data-category="boiserie">
        <img src="images/novas/projetos/boiserie/boiserie-04-recepcao-escritorio.jpg" alt="Moldura boiserie instalada em recepção e escritório corporativo" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Moldura Boiserie • Recepção & Escritório</div>
      </div>
      <div class="gitem ar-43 zoomable style-item" data-category="boiserie">
        <img src="images/novas/projetos/boiserie/boiserie-05-com-ripado.jpg" alt="Composição elegante de boiserie com ripado" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Moldura Boiserie • Composição com Ripado</div>
      </div>
      <div class="gitem ar-43 zoomable style-item" data-category="boiserie">
        <img src="images/novas/projetos/boiserie/boiserie-06-sala-espera-lounge.jpg" alt="Moldura boiserie clássica instalada em sala de espera e lounge elegante" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Moldura Boiserie • Sala de Espera & Lounge</div>
      </div>
    </div>"""

    c = re.sub(
        r'<div class="gallery gallery-3" data-anim>.*?</div>\s*</div>\s*</section>\s*<!-- ═══.*?CONSULTORIA',
        projetos_novo + "\n  </div>\n</section>\n\n<!-- ══════════════════════════════════════\n     CONSULTORIA",
        c,
        flags=re.DOTALL
    )

    # 6. Consultoria Imagem: Capa Papel de Parede Centralizada
    c = re.sub(
        r'<img src="images/consultoria-principal\.jpg" alt="[^"]*" loading="lazy">',
        '<img src="images/novas/capas/capa-papel-de-parede.jpg" alt="Ambiente planejado e transformado pela Aplik Decor" class="capa-centralizada" loading="lazy">',
        c
    )

    # 7. Diferenciais: Títulos em Caixa Alta, sem <br>, Acabamento Premium texto atualizado
    diferenciais_novo = """    <div class="why-grid">
      <div class="why-item" data-anim data-delay="1">
        <div class="why-icon" aria-hidden="true">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
        </div>
        <h3 class="why-title">ATENDIMENTO PERSONALIZADO</h3>
        <p class="why-desc">Entendemos o projeto antes de indicar a solução ideal para o seu espaço.</p>
      </div>
      <div class="why-item" data-anim data-delay="2">
        <div class="why-icon" aria-hidden="true">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <h3 class="why-title">QUALIDADE COMPROVADA</h3>
        <p class="why-desc">Produtos e acabamentos voltados para estética, funcionalidade e durabilidade.</p>
      </div>
      <div class="why-item" data-anim data-delay="3">
        <div class="why-icon" aria-hidden="true">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
        </div>
        <h3 class="why-title">SOLUÇÃO COMPLETA</h3>
        <p class="why-desc">Produto, orientação e instalação profissional. Do início ao acabamento final.</p>
      </div>
      <div class="why-item" data-anim data-delay="4">
        <div class="why-icon" aria-hidden="true">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
        </div>
        <h3 class="why-title">ACABAMENTO PREMIUM</h3>
        <p class="why-desc">Valorizamos cada detalhe, porque acreditamos que a excelência está no resultado final.</p>
      </div>
    </div>"""

    c = re.sub(
        r'<div class="why-grid">.*?</div>\s*</div>\s*</section>',
        diferenciais_novo + "\n  </div>\n</section>",
        c,
        flags=re.DOTALL
    )

    # 8. Depoimentos: 5 depoimentos completos com fotos em images/novas/feedbacks/
    depoimentos_novo = """    <div class="testimonials-grid" data-anim data-delay="2">
      <!-- Depoimento 1: Adriano Loos -->
      <div class="testimonial">
        <div>
          <div class="stars">★★★★★</div>
          <p class="testimonial-text">
            "Passando para agradecer pelo trabalho desempenhado aqui no meu consultório pelo Welber papel de parede com aplicação incrível, trouxe aqui uma sensação de leveza e bem-estar. Muito obrigado pelo profissionalismo, está recomendado"
          </p>
        </div>
        <div class="testimonial-author">
          <div class="testimonial-avatar">
            <img src="images/novas/feedbacks/cliente-01-adriano.jpg" alt="Foto Adriano Loos" loading="lazy">
          </div>
          <div>
            <div class="testimonial-name">Adriano Loos</div>
            <div class="testimonial-role">Psicólogo • Consultório em Primavera do Leste</div>
          </div>
        </div>
      </div>

      <!-- Depoimento 2: Roberto Pelegrini -->
      <div class="testimonial">
        <div>
          <div class="stars">★★★★★</div>
          <p class="testimonial-text">
            "Uelber muito obrigado, o papel ripado ficou excelente, com certeza faremos novamente em outros ambientes! A Vania adorou, ficou encantada."
          </p>
        </div>
        <div class="testimonial-author">
          <div class="testimonial-avatar">
            <img src="images/novas/feedbacks/cliente-02-roberto.jpg" alt="Foto Roberto Pelegrini" loading="lazy">
          </div>
          <div>
            <div class="testimonial-name">Roberto Pelegrini</div>
            <div class="testimonial-role">Pelegrini Representações • Primavera do Leste</div>
          </div>
        </div>
      </div>

      <!-- Depoimento 3: Edilene Souza -->
      <div class="testimonial">
        <div>
          <div class="stars">★★★★★</div>
          <p class="testimonial-text">
            "Uelber passando aqui pra dizer que amei o papel de parede líquido superou minha expectativa rsrs, ficou muito boa a parede !!"
          </p>
        </div>
        <div class="testimonial-author">
          <div class="testimonial-avatar">
            <img src="images/novas/feedbacks/cliente-03-edilene.jpg" alt="Foto Edilene Souza" loading="lazy">
          </div>
          <div>
            <div class="testimonial-name">Edilene Souza</div>
            <div class="testimonial-role">Quarto Casal • Primavera do Leste</div>
          </div>
        </div>
      </div>

      <!-- Depoimento 4: Mirian Luciano -->
      <div class="testimonial">
        <div>
          <div class="stars">★★★★★</div>
          <p class="testimonial-text">
            "Essa empresa é super recomendada, aqui em Rondonópolis eles prestam um serviço de excelência. Já faço serviço com eles há mais de 8 anos, sempre com qualidade, cumprimento de prazo e ótimos preços. Nossa parceria continua e em breve faremos novos projetos. Grata!"
          </p>
        </div>
        <div class="testimonial-author">
          <div class="testimonial-avatar">
            <img src="images/novas/feedbacks/cliente-04-mirian.jpg" alt="Foto Mirian Luciano" loading="lazy">
          </div>
          <div>
            <div class="testimonial-name">Mirian Luciano</div>
            <div class="testimonial-role">Rondonópolis MT</div>
          </div>
        </div>
      </div>

      <!-- Depoimento 5: Hellen Cristina -->
      <div class="testimonial">
        <div>
          <div class="stars">★★★★★</div>
          <p class="testimonial-text">
            "Só pra deixar registrado que meu lavabo ficou chique demais e o papel de parede linho realmente valorizou e ficou perfeito. Muito obrigado ao profissionalismo !!"
          </p>
        </div>
        <div class="testimonial-author">
          <div class="testimonial-avatar">
            <img src="images/novas/feedbacks/cliente-05-hellen.jpg" alt="Foto Hellen Cristina" loading="lazy">
          </div>
          <div>
            <div class="testimonial-name">Hellen Cristina</div>
            <div class="testimonial-role">Lavabo • Poxoréo MT</div>
          </div>
        </div>
      </div>
    </div>"""

    c = re.sub(
        r'<div class="testimonials-grid" data-anim data-delay="2">.*?</div>\s*</div>\s*</section>',
        depoimentos_novo + "\n  </div>\n</section>",
        c,
        flags=re.DOTALL
    )

    # 9. CTA Final: Título e subtítulo contínuos, botão em caixa alta
    c = re.sub(
        r'Quero Encontrar Minha Solução',
        'QUERO ENCONTRAR A MINHA SOLUÇÃO',
        c
    )

    # 10. FAQ: Título em Amarelo e Caixa Alta + Perguntas e Respostas oficiais
    faq_novo = """<section class="section section-dark" id="faq" aria-labelledby="faq-title">
  <div class="container">
    <div class="text-center" style="margin-bottom:52px">
      <div class="section-label" data-anim>Dúvidas Frequentes</div>
      <h2 class="section-title text-yellow" id="faq-title" data-anim data-delay="1" style="color: #e5a93c !important; text-transform: uppercase !important;">PERGUNTAS FREQUENTES</h2>
    </div>
    <div class="faq" style="max-width:800px;margin:0 auto" data-anim data-delay="2">
      <div class="faq-item">
        <button class="faq-btn" aria-expanded="false">
          Quais produtos Aplikdecor oferece?
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
        </button>
        <div class="faq-body">
          <div class="faq-body-inner">Trabalhamos com uma linha completa de soluções para transformar e valorizar seu ambiente, incluindo papéis de parede em diversos modelos, estilos e texturas, papel de parede líquido com várias opções de cores, piso vinílico disponível em diferentes cores, e molduras boiserie para um acabamento sofisticado e personalizado.</div>
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-btn" aria-expanded="false">
          Vocês realizam a instalação?
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
        </button>
        <div class="faq-body">
          <div class="faq-body-inner">Sim, para papel de parede, piso vinílico e molduras a instalação profissional já é inclusa.</div>
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-btn" aria-expanded="false">
          Quais cidades e regiões atendem?
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
        </button>
        <div class="faq-body">
          <div class="faq-body-inner">Nossa base é em Primavera do Leste MT. Mas atendemos também Campo Verde, Poxoréu, Rondonópolis, Paranatinga e outras cidades da região.</div>
        </div>
      </div>
    </div>
  </div>
</section>"""

    c = re.sub(
        r'<section class="section section-dark" id="faq".*?</section>',
        faq_novo,
        c,
        flags=re.DOTALL
    )

    # 11. Rodapé: Descrição da empresa, sequência da coluna produtos, endereço e telefone
    rodape_novo = """<footer class="footer" aria-label="Rodapé">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo" aria-label="Aplik Decor - Início">
          <img src="images/logo-aplik-horizontal.png" alt="Aplik Decor" class="logo-img">
        </a>
        <p>Especialista em transformação de ambientes há mais de 12 anos em Primavera do Leste.</p>
      </div>

      <nav aria-label="Links rápidos do rodapé">
        <div class="footer-title">Produtos</div>
        <div class="footer-links">
          <a href="papel-de-parede.html" data-cta="papel">Papel de parede</a>
          <a href="papel-de-parede.html#variedade" data-cta="papel">Papel de parede líquido</a>
          <a href="papel-de-parede.html#variedade" data-cta="papel">Pedras naturais</a>
          <a href="piso-vinilico.html" data-cta="piso">Piso vinílico</a>
          <a href="boiserie.html" data-cta="boiserie">Moldura Boiserie</a>
          <a href="#projetos">Projetos</a>
        </div>
      </nav>

      <div>
        <div class="footer-title">Contato & Localização</div>
        <div class="footer-contact">
          <div class="footer-contact-item">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            <p>Rua Rafael Borgetti, Nº 110, Bairro Castelândia - Primavera do Leste MT / CEP: 78.850-000</p>
          </div>
          <div class="footer-contact-item">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            <p><a href="tel:66996706972" style="color:inherit">(66) 99670-6972</a></p>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <span>© 2026 Aplik Decor. Todos os direitos reservados.</span>
      <span>Primavera do Leste, Mato Grosso</span>
    </div>
  </div>
</footer>"""

    c = re.sub(
        r'<footer class="footer" aria-label="Rodapé">.*?</footer>',
        rodape_novo,
        c,
        flags=re.DOTALL
    )

    with open(p_index, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(c)
    print("[OK] index.html atualizado com sucesso!")


def atualizar_papel_de_parede_html(repo_dir):
    p_lp = os.path.join(repo_dir, "papel-de-parede.html")
    if not os.path.exists(p_lp):
        print("papel-de-parede.html não encontrado!")
        return

    with open(p_lp, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()

    # 1. Navegação no Header (Sequência oficial: Papel de Parede, Piso Vinílico, Moldura Boiserie)
    nav_header = """      <nav class="nav" aria-label="Navegação">
        <a href="papel-de-parede.html" class="active">Papel de Parede</a>
        <a href="piso-vinilico.html">Piso Vinílico</a>
        <a href="boiserie.html">Moldura Boiserie</a>
        <a href="#projetos">Projetos</a>
        <a href="#faq">Dúvidas</a>
        <a href="index.html" class="nav-back">← Início</a>
      </nav>"""
    c = re.sub(
        r'<nav class="nav" aria-label="Navegação">.*?</nav>',
        nav_header,
        c,
        flags=re.DOTALL
    )

    nav_mobile = """<nav class="mobile-menu" id="mobile-menu" aria-label="Menu mobile">
  <a href="papel-de-parede.html">Papel de Parede</a>
  <a href="piso-vinilico.html">Piso Vinílico</a>
  <a href="boiserie.html">Moldura Boiserie</a>
  <a href="#projetos">Projetos</a>
  <a href="#faq">Dúvidas</a>
  <a href="index.html">← Voltar ao Início</a>
  <a href="#" class="btn btn-gold" data-cta="form">Falar com Especialista</a>
</nav>"""
    c = re.sub(
        r'<nav class="mobile-menu" id="mobile-menu" aria-label="Menu mobile">.*?</nav>',
        nav_mobile,
        c,
        flags=re.DOTALL
    )

    # 2. Hero Background e Consultoria: Capa Papel de Parede Centralizada
    c = re.sub(
        r'<div class="hero-bg">\s*<img src="[^"]*"[^>]*>',
        '<div class="hero-bg">\n    <img src="images/novas/capas/capa-papel-de-parede.jpg" alt="Papel de parede instalado pela Aplik Decor" class="capa-centralizada" loading="eager" fetchpriority="high">',
        c
    )
    c = re.sub(
        r'<div class="img-frame zoomable"[^>]*>\s*<img src="[^"]*"[^>]*>',
        '<div class="img-frame zoomable" style="aspect-ratio:4/3">\n          <img src="images/novas/capas/capa-papel-de-parede.jpg" alt="Papel de parede instalado em destaque" class="capa-centralizada" loading="lazy">',
        c
    )

    # 3. Galeria de Projetos: 6 fotos oficiais
    galeria_novo = """    <div class="gallery gallery-3" data-anim>
      <div class="gitem ar-43 zoomable">
        <img src="images/novas/projetos/papel-de-parede/papel-01-ripado-marmorizado.jpg" alt="Papel de parede ripado e marmorizado aplicado pela Aplik Decor" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Papel de Parede • Ripado e Marmorizado</div>
      </div>
      <div class="gitem ar-43 zoomable">
        <img src="images/novas/projetos/papel-de-parede/papel-02-quarto-menina.jpg" alt="Papel de parede quarto de menina instalado pela Aplik Decor" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Papel de Parede • Quarto de Menina</div>
      </div>
      <div class="gitem ar-43 zoomable">
        <img src="images/novas/projetos/papel-de-parede/papel-03-tradicional-ripado.jpg" alt="Papel de parede tradicional ripado aplicado pela Aplik Decor" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Papel de Parede • Tradicional Ripado Nobre</div>
      </div>
      <div class="gitem ar-43 zoomable">
        <img src="images/novas/projetos/papel-de-parede/papel-04-tradicional-linho.jpg" alt="Papel de parede textura linho instalado pela Aplik Decor" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Papel de Parede • Tradicional Linho</div>
      </div>
      <div class="gitem ar-43 zoomable">
        <img src="images/novas/projetos/papel-de-parede/papel-05-papel-liquido.jpg" alt="Papel de parede líquido aplicado pela Aplik Decor" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Papel de Parede • Textura Papel Líquido</div>
      </div>
      <div class="gitem ar-43 zoomable">
        <img src="images/novas/projetos/papel-de-parede/papel-06-estampado-lavabo.jpg" alt="Papel de parede estampado para lavabo aplicado pela Aplik Decor" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Papel de Parede • Estampado Exclusivo Lavabo</div>
      </div>
    </div>"""

    c = re.sub(
        r'<div class="gallery gallery-3" data-anim>.*?</div>\s*</div>\s*</section>',
        galeria_novo + "\n  </div>\n</section>",
        c,
        flags=re.DOTALL
    )

    # 4. Rodapé padronizado
    rodape_novo = """<footer class="footer" aria-label="Rodapé">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo">
          <img src="images/logo-aplik-horizontal.png" alt="Aplik Decor" class="logo-img">
        </a>
        <p>Especialista em transformação de ambientes há mais de 12 anos em Primavera do Leste.</p>
      </div>
      <div>
        <div class="footer-title">Produtos</div>
        <div class="footer-links">
          <a href="index.html">← Página Inicial</a>
          <a href="papel-de-parede.html" data-cta="papel">Papel de parede</a>
          <a href="papel-de-parede.html#variedade" data-cta="papel">Papel de parede líquido</a>
          <a href="papel-de-parede.html#variedade" data-cta="papel">Pedras naturais</a>
          <a href="piso-vinilico.html" data-cta="piso">Piso Vinílico</a>
          <a href="boiserie.html" data-cta="boiserie">Moldura Boiserie</a>
        </div>
      </div>
      <div>
        <div class="footer-title">Contato & Localização</div>
        <div class="footer-contact">
          <div class="footer-contact-item">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            <p>Rua Rafael Borgetti, Nº 110, Bairro Castelândia - Primavera do Leste MT / CEP: 78.850-000</p>
          </div>
          <div class="footer-contact-item">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            <p><a href="tel:66996706972" style="color:inherit">(66) 99670-6972</a></p>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Aplik Decor. Todos os direitos reservados.</span>
      <span>Primavera do Leste, Mato Grosso</span>
    </div>
  </div>
</footer>"""

    c = re.sub(
        r'<footer class="footer" aria-label="Rodapé">.*?</footer>',
        rodape_novo,
        c,
        flags=re.DOTALL
    )

    with open(p_lp, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(c)
    print("[OK] papel-de-parede.html atualizado com sucesso!")


def atualizar_piso_vinilico_html(repo_dir):
    p_lp = os.path.join(repo_dir, "piso-vinilico.html")
    if not os.path.exists(p_lp):
        print("piso-vinilico.html não encontrado!")
        return

    with open(p_lp, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()

    # 1. Navegação no Header (Sequência oficial: Papel de Parede, Piso Vinílico, Moldura Boiserie)
    nav_header = """      <nav class="nav" aria-label="Navegação">
        <a href="papel-de-parede.html">Papel de Parede</a>
        <a href="piso-vinilico.html" class="active">Piso Vinílico</a>
        <a href="boiserie.html">Moldura Boiserie</a>
        <a href="#beneficios">Benefícios</a>
        <a href="#ambientes">Galeria</a>
        <a href="#faq">Dúvidas</a>
        <a href="index.html" class="nav-back">← Início</a>
      </nav>"""
    c = re.sub(
        r'<nav class="nav" aria-label="Navegação">.*?</nav>',
        nav_header,
        c,
        flags=re.DOTALL
    )

    nav_mobile = """<nav class="mobile-menu" id="mobile-menu" aria-label="Menu mobile">
  <a href="papel-de-parede.html">Papel de Parede</a>
  <a href="piso-vinilico.html">Piso Vinílico</a>
  <a href="boiserie.html">Moldura Boiserie</a>
  <a href="#beneficios">Benefícios</a>
  <a href="#ambientes">Galeria</a>
  <a href="#faq">Dúvidas</a>
  <a href="index.html">← Voltar ao Início</a>
  <a href="#" class="btn btn-gold" data-cta="form">Falar com Especialista</a>
</nav>"""
    c = re.sub(
        r'<nav class="mobile-menu" id="mobile-menu" aria-label="Menu mobile">.*?</nav>',
        nav_mobile,
        c,
        flags=re.DOTALL
    )

    # 2. Hero Background e Consultoria: Capa Piso Vinílico Centralizada
    c = re.sub(
        r'<div class="hero-bg">\s*<img src="[^"]*"[^>]*>',
        '<div class="hero-bg">\n    <img src="images/novas/capas/capa-piso-vinilico.jpg" alt="Piso Vinílico instalado pela Aplik Decor" class="capa-centralizada" loading="eager" fetchpriority="high">',
        c
    )
    c = re.sub(
        r'<div class="img-frame zoomable"[^>]*>\s*<img src="[^"]*"[^>]*>',
        '<div class="img-frame zoomable" style="aspect-ratio:4/3">\n          <img src="images/novas/capas/capa-piso-vinilico.jpg" alt="Piso vinílico instalado pela Aplik Decor" class="capa-centralizada" loading="lazy">',
        c
    )

    # 3. Galeria de Projetos: 3 Fotos Oficiais (sem duplicidade)
    galeria_novo = """    <div class="gallery gallery-3" data-anim>
      <div class="gitem ar-43 zoomable">
        <img src="images/novas/projetos/piso-vinilico/piso-01-ambiente-instalado.jpg" alt="Piso Vinílico em sala de estar e ambientes integrados" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Piso Vinílico • Sala & Ambientes Integrados</div>
      </div>
      <div class="gitem ar-43 zoomable">
        <img src="images/novas/projetos/piso-vinilico/piso-02-mostruario-padroes.jpg" alt="Mostruário de padrões e cores de piso vinílico" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Piso Vinílico • Mostruário de Padrões e Cores</div>
      </div>
      <div class="gitem ar-43 zoomable">
        <img src="images/novas/projetos/piso-vinilico/piso-03-living-amadeirado.jpg" alt="Piso vinílico living amadeirado de alto padrão instalado" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Piso Vinílico • Living Amadeirado</div>
      </div>
    </div>"""

    c = re.sub(
        r'<div class="gallery (?:gallery-4|gallery-3)" data-anim>.*?</div>\s*</div>\s*</section>',
        galeria_novo + "\n  </div>\n</section>",
        c,
        flags=re.DOTALL
    )

    # 4. Rodapé padronizado
    rodape_novo = """<footer class="footer" aria-label="Rodapé">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo">
          <img src="images/logo-aplik-horizontal.png" alt="Aplik Decor" class="logo-img">
        </a>
        <p>Especialista em transformação de ambientes há mais de 12 anos em Primavera do Leste.</p>
      </div>
      <div>
        <div class="footer-title">Produtos</div>
        <div class="footer-links">
          <a href="index.html">← Página Inicial</a>
          <a href="papel-de-parede.html" data-cta="papel">Papel de Parede</a>
          <a href="papel-de-parede.html#variedade" data-cta="papel">Papel de parede líquido</a>
          <a href="piso-vinilico.html" data-cta="piso">Piso Vinílico</a>
          <a href="boiserie.html" data-cta="boiserie">Moldura Boiserie</a>
        </div>
      </div>
      <div>
        <div class="footer-title">Contato & Localização</div>
        <div class="footer-contact">
          <div class="footer-contact-item">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            <p>Rua Rafael Borgetti, Nº 110, Bairro Castelândia - Primavera do Leste MT / CEP: 78.850-000</p>
          </div>
          <div class="footer-contact-item">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            <p><a href="tel:66996706972" style="color:inherit">(66) 99670-6972</a></p>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Aplik Decor. Todos os direitos reservados.</span>
      <span>Primavera do Leste, Mato Grosso</span>
    </div>
  </div>
</footer>"""

    c = re.sub(
        r'<footer class="footer" aria-label="Rodapé">.*?</footer>',
        rodape_novo,
        c,
        flags=re.DOTALL
    )

    with open(p_lp, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(c)
    print("[OK] piso-vinilico.html atualizado com sucesso!")


def atualizar_boiserie_html(repo_dir):
    p_lp = os.path.join(repo_dir, "boiserie.html")
    if not os.path.exists(p_lp):
        print("boiserie.html não encontrado!")
        return

    with open(p_lp, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()

    # 1. Navegação no Header (Sequência oficial: Papel de Parede, Piso Vinílico, Moldura Boiserie)
    nav_header = """      <nav class="nav" aria-label="Navegação">
        <a href="papel-de-parede.html">Papel de Parede</a>
        <a href="piso-vinilico.html">Piso Vinílico</a>
        <a href="boiserie.html" class="active">Moldura Boiserie</a>
        <a href="#o-que-e">O Que É</a>
        <a href="#modelos">Modelos</a>
        <a href="#projetos">Projetos</a>
        <a href="#faq">Dúvidas</a>
        <a href="index.html" class="nav-back">← Início</a>
      </nav>"""
    c = re.sub(
        r'<nav class="nav" aria-label="Navegação">.*?</nav>',
        nav_header,
        c,
        flags=re.DOTALL
    )

    nav_mobile = """<nav class="mobile-menu" id="mobile-menu" aria-label="Menu mobile">
  <a href="papel-de-parede.html">Papel de Parede</a>
  <a href="piso-vinilico.html">Piso Vinílico</a>
  <a href="boiserie.html">Moldura Boiserie</a>
  <a href="#o-que-e">O Que É</a>
  <a href="#modelos">Modelos</a>
  <a href="#projetos">Projetos</a>
  <a href="#faq">Dúvidas</a>
  <a href="index.html">← Voltar ao Início</a>
  <a href="#" class="btn btn-gold" data-cta="form">Falar com Especialista</a>
</nav>"""
    c = re.sub(
        r'<nav class="mobile-menu" id="mobile-menu" aria-label="Menu mobile">.*?</nav>',
        nav_mobile,
        c,
        flags=re.DOTALL
    )

    # 2. Hero Background e Imagens de Destaque: Capa Boiserie Centralizada
    c = re.sub(
        r'<div class="hero-bg">\s*<img src="[^"]*"[^>]*>',
        '<div class="hero-bg">\n    <img src="images/novas/capas/capa-moldura-boiserie.jpg" alt="Moldura Boiserie instalada pela Aplik Decor" class="capa-centralizada" loading="eager" fetchpriority="high">',
        c
    )
    c = re.sub(
        r'<div class="img-frame zoomable" style="aspect-ratio:3/4">\s*<img src="[^"]*"[^>]*>',
        '<div class="img-frame zoomable" style="aspect-ratio:3/4">\n          <img src="images/novas/capas/capa-moldura-boiserie.jpg" alt="Moldura Boiserie em destaque" class="capa-centralizada" loading="lazy">',
        c
    )
    c = c.replace('images/img35.jpeg', 'images/novas/projetos/boiserie/boiserie-03-personalizado-luxo.jpg')

    # 3. Galeria de Projetos: 6 fotos oficiais
    galeria_novo = """    <div class="gallery gallery-3" data-anim>
      <div class="gitem ar-43 zoomable">
        <img src="images/novas/projetos/boiserie/boiserie-01-painel-geometrico.jpg" alt="Moldura boiserie painel geométrico moderno instalado pela Aplik Decor" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Moldura Boiserie • Painel Geométrico Moderno</div>
      </div>
      <div class="gitem ar-43 zoomable">
        <img src="images/novas/projetos/boiserie/boiserie-02-com-papel-liquido.jpg" alt="Moldura boiserie combinada com papel líquido" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Moldura Boiserie • Boiserie com Papel Líquido</div>
      </div>
      <div class="gitem ar-43 zoomable">
        <img src="images/novas/projetos/boiserie/boiserie-03-personalizado-luxo.jpg" alt="Moldura boiserie em painel de alto padrão de luxo" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Moldura Boiserie • Painel de Alto Padrão</div>
      </div>
      <div class="gitem ar-43 zoomable">
        <img src="images/novas/projetos/boiserie/boiserie-04-recepcao-escritorio.jpg" alt="Moldura boiserie instalada em recepção e escritório corporativo" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Moldura Boiserie • Recepção & Escritório</div>
      </div>
      <div class="gitem ar-43 zoomable">
        <img src="images/novas/projetos/boiserie/boiserie-05-com-ripado.jpg" alt="Composição sofisticada de boiserie com ripado" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Moldura Boiserie • Composição com Ripado</div>
      </div>
      <div class="gitem ar-43 zoomable">
        <img src="images/novas/projetos/boiserie/boiserie-06-sala-espera-lounge.jpg" alt="Moldura boiserie clássica instalada em sala de espera e lounge elegante" loading="lazy">
        <div class="gitem-overlay"></div>
        <div class="gitem-label">Moldura Boiserie • Sala de Espera & Lounge</div>
      </div>
    </div>"""

    c = re.sub(
        r'<div class="gallery gallery-3" data-anim>.*?</div>\s*</div>\s*</section>',
        galeria_novo + "\n  </div>\n</section>",
        c,
        flags=re.DOTALL
    )

    # 4. Rodapé padronizado
    rodape_novo = """<footer class="footer" aria-label="Rodapé">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo">
          <img src="images/logo-aplik-horizontal.png" alt="Aplik Decor" class="logo-img">
        </a>
        <p>Especialista em transformação de ambientes há mais de 12 anos em Primavera do Leste.</p>
      </div>
      <div>
        <div class="footer-title">Produtos</div>
        <div class="footer-links">
          <a href="index.html">← Página Inicial</a>
          <a href="papel-de-parede.html" data-cta="papel">Papel de Parede</a>
          <a href="piso-vinilico.html" data-cta="piso">Piso Vinílico</a>
          <a href="boiserie.html" data-cta="boiserie">Moldura Boiserie</a>
        </div>
      </div>
      <div>
        <div class="footer-title">Contato & Localização</div>
        <div class="footer-contact">
          <div class="footer-contact-item">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            <p>Rua Rafael Borgetti, Nº 110, Bairro Castelândia - Primavera do Leste MT / CEP: 78.850-000</p>
          </div>
          <div class="footer-contact-item">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            <p><a href="tel:66996706972" style="color:inherit">(66) 99670-6972</a></p>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Aplik Decor. Todos os direitos reservados.</span>
      <span>Primavera do Leste, Mato Grosso</span>
    </div>
  </div>
</footer>"""

    c = re.sub(
        r'<footer class="footer" aria-label="Rodapé">.*?</footer>',
        rodape_novo,
        c,
        flags=re.DOTALL
    )

    with open(p_lp, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(c)
    print("[OK] boiserie.html atualizado com sucesso!")


def aplicar():
    if os.path.exists("index.html"):
        repo_dir = "."
    elif os.path.exists("../index.html"):
        repo_dir = ".."
    else:
        repo_dir = r"C:\Projetos\Pixel\Landing Pages\Aplik Decor"

    print(f"Diretório do repositório detectado: {os.path.abspath(repo_dir)}\n")

    atualizar_style_css(repo_dir)
    atualizar_index_html(repo_dir)
    atualizar_papel_de_parede_html(repo_dir)
    atualizar_piso_vinilico_html(repo_dir)
    atualizar_boiserie_html(repo_dir)

    print("\n[OK] Todas as atualizações foram aplicadas com sucesso nas 4 LPs e no style.css!")

if __name__ == '__main__':
    aplicar()
