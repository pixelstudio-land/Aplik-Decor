/* ============================================
   APLIK DECOR — SCRIPT GLOBAL
   ============================================ */

// ⚠️ SUBSTITUIR PELO LINK DO FORMULÁRIO DO CLIENTE
const CTA_URL = "https://SEU-FORMULARIO-AQUI.com";

// Link do WhatsApp
const WA_URL = "https://wa.me/message/SRJLDHRBIWGQF1";

// URLs das LPs específicas
const LP = {
  piso:     "./piso-vinilico.html",
  boiserie: "./boiserie.html",
  papel:    "./papel-de-parede.html"
};

/* ── CTA Links ─────────────────────────── */
function applyCTA() {
  document.querySelectorAll("[data-cta='form']").forEach(el => {
    el.href = CTA_URL;
    el.target = "_blank";
    el.rel = "noopener noreferrer";
  });
  document.querySelectorAll("[data-cta='whatsapp']").forEach(el => {
    el.href = WA_URL;
    el.target = "_blank";
    el.rel = "noopener noreferrer";
  });
  document.querySelectorAll("[data-cta='piso']").forEach(el => { el.href = LP.piso });
  document.querySelectorAll("[data-cta='boiserie']").forEach(el => { el.href = LP.boiserie });
  document.querySelectorAll("[data-cta='papel']").forEach(el => { el.href = LP.papel });
}

/* ── Header scroll ─────────────────────── */
function initHeader() {
  const h = document.querySelector(".header");
  if (!h) return;
  const onScroll = () => h.classList.toggle("scrolled", window.scrollY > 48);
  window.addEventListener("scroll", onScroll, { passive: true });
}

/* ── Mobile menu ───────────────────────── */
function initMenu() {
  const btn  = document.getElementById("menu-toggle");
  const menu = document.getElementById("mobile-menu");
  if (!btn || !menu) return;

  btn.addEventListener("click", () => {
    const open = menu.classList.toggle("open");
    btn.classList.toggle("open", open);
    btn.setAttribute("aria-expanded", open);
    document.body.style.overflow = open ? "hidden" : "";
  });

  menu.querySelectorAll("a").forEach(a => {
    a.addEventListener("click", () => {
      menu.classList.remove("open");
      btn.classList.remove("open");
      document.body.style.overflow = "";
    });
  });
}

/* ── FAQ Accordion ─────────────────────── */
function initFAQ() {
  document.querySelectorAll(".faq-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const item = btn.closest(".faq-item");
      const body = item.querySelector(".faq-body");
      const isOpen = item.classList.contains("open");

      // Fechar todos
      document.querySelectorAll(".faq-item.open").forEach(el => {
        el.classList.remove("open");
        el.querySelector(".faq-body").style.maxHeight = "0";
      });

      // Abrir clicado (se estava fechado)
      if (!isOpen) {
        item.classList.add("open");
        body.style.maxHeight = body.scrollHeight + "px";
      }
    });
  });
}

/* ── Scroll animations ─────────────────── */
function initAnimations() {
  const io = new IntersectionObserver(
    (entries) => entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add("on");
        io.unobserve(e.target);
      }
    }),
    { threshold: 0.08, rootMargin: "0px 0px -32px 0px" }
  );
  document.querySelectorAll("[data-anim]").forEach(el => io.observe(el));
}

/* ── Init ──────────────────────────────── */
document.addEventListener("DOMContentLoaded", () => {
  applyCTA();
  initHeader();
  initMenu();
  initFAQ();
  initAnimations();
});
