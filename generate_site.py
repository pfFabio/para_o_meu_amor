import os
import json

base_dir = r"c:\Users\Usuario\Documents\viagem 2026\viagem de maio-2026"

sections = {
    "aniversário": {"title": "Meu Aniversário", "desc": "Comemorar meu aniversário ao seu lado tornou esse dia um dos mais especiais e felizes da minha vida."},
    "darwin": {"title": "Caminho de Darwin", "desc": "Nossa subida histórica! O esforço valeu a pena só para ter essa vista incrível e sua companhia maravilhosa."},
    "telégrafo": {"title": "Morro do Telégrafo", "desc": "A trilha no Morro do Telégrafo foi mais uma aventura linda nossa. Cada passo juntos fortalece nossa conexão."},
    "yoga": {"title": "Aula de Yoga", "desc": "Nossa aula de yoga trouxe um momento de paz e equilíbrio, nos conectando ainda mais."},
    "di_italia": {"title": "Restaurante Di Italia", "desc": "Nossa romântica ida ao Di Italia... Momentos deliciosos regados a boas conversas e a melhor companhia."},
    "recanto": {"title": "Praia do Recanto", "desc": "O restaurante na praia fechou nossos passeios com chave de ouro. A brisa do mar e o seu sorriso!"},
    "farol ponta negra": {"title": "Farol de Ponta Negra", "desc": "Mais um cenário incrível que tivemos o prazer de explorar juntos."},
    "queijos e vinhos": {"title": "Queijos e Vinhos", "desc": "Uma noite especial e saborosa, um brinde ao nosso amor!"},
}

details = {
    "pulseiras": {"title": "A Pulseira Dourada", "icon": "fa-link", "desc": "as correntes que ligam nossas almas"},
    "com a sogra": {"title": "Lanche em Família", "icon": "fa-mug-hot", "desc": "Ver você lanchando com a minha mãe encheu meu coração de alegria."},
    "fone de ouvido": {"title": "O Fone de Ouvido", "icon": "fa-headphones", "desc": "Obrigado por esse presente incrível, eu amo usar todo dia!"}
}

html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Para Minha Gatinha, Izi ❤️</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="hearts-bg" id="hearts-bg"></div>

    <header class="hero">
        <div class="hero-bg" style="background-image: url('viagem de maio-2026/{hero_image}');"></div>
        <div class="hero-overlay"></div>
        <div class="hero-content reveal">
            <h2 class="pre-title">Para a minha</h2>
            <h1 class="title">Gatinha</h1>
            <p class="subtitle">Cada momento com você é uma nova página inesquecível da nossa história, Izi.</p>
            <div class="scroll-down">
                <span>Nossas Memórias</span>
                <i class="fa-solid fa-chevron-down"></i>
            </div>
        </div>
    </header>

    <main>
        <!-- Momentos em Pastas -->
        {event_sections}

        <!-- Fotos de Casal -->
        <section class="gallery-section">
            <div class="container">
                <div class="section-header reveal">
                    <h2>Nós Dois</h2>
                    <p>Momentos só nossos, cheios de amor</p>
                    <div class="separator"><i class="fa-solid fa-heart"></i></div>
                </div>
                <div class="masonry-grid reveal">
                    {casal_photos}
                </div>
            </div>
        </section>

        <!-- Detalhes (Pulseiras, Sogra, Fone) -->
        <section class="details-section">
            <div class="container">
                <div class="section-header reveal text-light">
                    <h2>Pequenos Grandes Detalhes</h2>
                    <p>Coisas que guardo no coração</p>
                    <div class="separator light"><i class="fa-solid fa-star"></i></div>
                </div>

                <div class="cards-grid">
                    {details_sections}
                </div>
            </div>
        </section>

        <section class="love-letter-section">
            <div class="container">
                <div class="letter-box reveal">
                    <div class="wax-seal"><i class="fa-solid fa-heart"></i></div>
                    <h2>Meu amor,</h2>
                    <div class="letter-content">
                        <p>Eu queria tirar um momento para te agradecer de verdade por tudo.</p>
                        <p>Obrigado pelos momentos incríveis que você me deu, eu amei demais! Mas acima de tudo, quero te agradecer pela confiança.</p>
                        <p>Obrigado por confiar em mim e ter ficado na minha casa. Esses dias ao seu lado foram mágicos e mal posso esperar para vivermos muitas outras aventuras juntos.</p>
                    </div>
                    <div class="signature">
                        Com todo o meu coração,<br>
                        <strong>Francisgleibison</strong>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>Feito com ❤️ por Fábio para sua Gatinha Izi &copy; 2026</p>
    </footer>

    <!-- Audio Player -->
    <audio id="bg-music" loop>
        <source src="musica.mp3" type="audio/mpeg">
    </audio>
    <button class="music-toggle" id="music-toggle" title="Tocar/Pausar Música">
        <i class="fa-solid fa-music"></i>
    </button>

    <div class="lightbox" id="lightbox">
        <button class="lightbox-close" id="lightbox-close"><i class="fa-solid fa-xmark"></i></button>
        <img src="" alt="Ampliada" id="lightbox-img">
    </div>

    <script src="script.js"></script>
</body>
</html>
"""

def is_image(filename):
    return filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))

casal_images = [f for f in os.listdir(base_dir) if os.path.isfile(os.path.join(base_dir, f)) and is_image(f)]
hero_image = "1780942377195.jpg"

casal_html = ""
for img in casal_images:
    casal_html += f'<div class="masonry-item"><img src="viagem de maio-2026/{img}" alt="Nós" loading="lazy"></div>\n'

event_html = ""
for folder, data in sections.items():
    folder_path = os.path.join(base_dir, folder)
    if os.path.isdir(folder_path):
        images = [f for f in os.listdir(folder_path) if is_image(f)]
        if images:
            grid_html = ""
            for img in images:
                grid_html += f'<div class="masonry-item"><img src="viagem de maio-2026/{folder}/{img}" alt="{data["title"]}" loading="lazy"></div>\n'
            
            layout_class = "masonry-grid"
            if folder == "aniversário":
                layout_class = "aniversario-grid"

            event_html += f'''
        <section class="gallery-section event-section">
            <div class="container">
                <div class="section-header reveal">
                    <h2>{data["title"]}</h2>
                    <p>{data["desc"]}</p>
                    <div class="separator"><i class="fa-solid fa-camera"></i></div>
                </div>
                <div class="{layout_class} reveal">
                    {grid_html}
                </div>
            </div>
        </section>
'''

details_html = ""
for folder, data in details.items():
    folder_path = os.path.join(base_dir, folder)
    if os.path.isdir(folder_path):
        images = [f for f in os.listdir(folder_path) if is_image(f)]
        if images:
            # We use a mini slider or just masonry for details. Since it's inside cards, let's just make the card show the first image, and maybe a small grid if multiple.
            # To keep the design elegant, let's just use the first image as the cover, but if there are multiple, user can see them in a tiny grid inside the card.
            img_html = f'<img src="viagem de maio-2026/{folder}/{images[0]}" alt="{data["title"]}">'
            
            details_html += f'''
                    <div class="glass-card reveal">
                        <div class="card-img">
                            {img_html}
                        </div>
                        <div class="card-body">
                            <div class="icon-wrap"><i class="fa-solid {data["icon"]}"></i></div>
                            <h3>{data["title"]}</h3>
                            <p>{data["desc"]}</p>
                        </div>
                    </div>
'''

final_html = html_template.format(
    hero_image=hero_image,
    casal_photos=casal_html,
    event_sections=event_html,
    details_sections=details_html
)

with open(r"c:\Users\Usuario\Documents\viagem 2026\index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Site generated successfully!")
