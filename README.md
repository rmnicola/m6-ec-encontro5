[Voltar para o repositório principal :house:](https://github.com/rmnicola/m6-ec-encontros.git)

# Visão computacional e Open CV <!-- omit in toc -->

## Objetivos do encontro
* Introduzir o que é uma imagem e sua representação computacional.
* Apresentar os conceitos básicos da visão computacional.
* Instalar e apresentar a biblioteca OpenCV.
* Utilizar a biblioteca OpenCV para fazer manipulação de imagens e usar filtros convolucionais.

## Conteúdo <!-- omit in toc -->

- [Objetivos do encontro](#objetivos-do-encontro)
- [Imagens digitais](#imagens-digitais)
- [OpenCV](#opencv)
- [Processamento básico de imagens](#processamento-básico-de-imagens)
- [Convolução matricial](#convolução-matricial)
- [Filtros convolucionais](#filtros-convolucionais)

## Imagens digitais

<img src="https://www.howtogeek.com/wp-content/uploads/2012/12/pixels-on-monitor.jpg?width=1198&trim=1,1&bg-color=000&pad=1,1" alt="Imagem" style="display: block; margin: 0 auto; width: 90%;">
<p style="margin-left: 15%">Imagem retirada de <a href="https://www.howtogeek.com/130826/how-to-fix-a-stuck-pixel-on-an-lcd-monitor/">Howtogeek</a></p>

As imagens digitais são representações visuais de dados que podem ser exibidas e processadas por meio de dispositivos eletrônicos, como computadores e smartphones. Essas imagens são compostas por pixels, que são pequenos pontos ou elementos individuais que formam a imagem completa. Cada pixel é atribuído a uma cor específica, e a forma como essas cores são representadas é fundamental para a qualidade e a precisão da imagem.

<img src="https://miro.medium.com/v2/resize:fit:640/0*fRubLY5Q3_YRMpK1" alt="Imagem" style="display: block; margin: 0 auto; width: 60%;">
<p style="margin-left: 15%">Imagem retirada de <a href="https://towardsdatascience.com/how-color-is-represented-and-viewed-in-computer-vision-b1cc97681b68">Towards Data Science</a></p>

Uma das formas mais comuns de representação de cores em imagens digitais é o sistema RGB (Red, Green, Blue), também conhecido como aditivo. Nesse sistema, cada pixel é definido por três componentes de cores primárias: vermelho, verde e azul. Cada componente varia de 0 a 255, representando a intensidade da cor. A combinação dessas três cores em diferentes níveis de intensidade permite criar uma ampla gama de cores e tons.

<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*RS3lOrpJc6bVSeNRzuZLpg.png" alt="Imagem" style="display: block; margin: 0 auto; width: 90%;">
<p style="margin-left: 15%">Imagem retirada de <a href="https://towardsdatascience.com/how-color-is-represented-and-viewed-in-computer-vision-b1cc97681b68">Towards Data Science</a></p>

Outro sistema de representação de cores é o CMYK (Ciano, Magenta, Amarelo, Preto), conhecido como subtrativo. Ele é amplamente utilizado em impressões e design gráfico. No sistema CMYK, as cores são obtidas pela mistura de tintas ciano, magenta, amarelo e preto. A combinação dessas cores em diferentes proporções resulta em uma gama de cores que podem ser reproduzidas na impressão.

<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/0*uoVxdnLhjwycG0jD.png" alt="Imagem" style="display: block; margin: 0 auto; width: 70%;">
<p style="margin-left: 15%">Imagem retirada de <a href="https://towardsdatascience.com/how-color-is-represented-and-viewed-in-computer-vision-b1cc97681b68">Towards Data Science</a></p>

Além do RGB e CMYK, existem sistemas de cores conhecidos como HSL (Hue, Saturation, Lightness) e HSV (Hue, Saturation, Value). Esses sistemas são usados principalmente para descrever as características perceptivas das cores. No HSL, a matiz (hue) representa a cor em si, a saturação (saturation) indica a pureza da cor e a luminosidade (lightness) determina o brilho da cor. No sistema HSV, a diferença é que a luminosidade é substituída pelo valor (value), que também define o brilho, mas de uma maneira diferente.

Esses diferentes sistemas de representação de cores oferecem flexibilidade para a manipulação e exibição de imagens digitais em diversos contextos. Cada sistema possui suas aplicações específicas, e o conhecimento sobre essas representações é essencial para a criação e a edição de imagens de alta qualidade e para a garantia de resultados precisos em impressões e exibições em dispositivos eletrônicos.

## OpenCV

OpenCV (Open Source Computer Vision Library) é uma biblioteca de visão computacional de código aberto amplamente utilizada para processamento de imagens e análise visual. Desenvolvida originalmente pela Intel, a biblioteca oferece um conjunto abrangente de ferramentas e algoritmos otimizados para trabalhar com imagens e vídeos em tempo real. O OpenCV é escrito em C++ e possui interfaces para várias linguagens de programação, incluindo Python e Java, o que o torna acessível e versátil para desenvolvedores de diferentes áreas.

O objetivo principal do OpenCV é fornecer um conjunto de funções e algoritmos que facilitem a implementação de aplicações de visão computacional, como detecção de objetos, reconhecimento facial, calibração de câmera, rastreamento de movimento, entre outros. A biblioteca suporta uma ampla variedade de plataformas, incluindo Windows, Linux, macOS, Android e iOS, permitindo a criação de soluções multiplataforma. Com sua vasta gama de recursos e suporte a hardware acelerado, o OpenCV tornou-se uma referência no campo da visão computacional e é amplamente adotado em projetos acadêmicos, industriais e de pesquisa.

Para instalar o OpenCV, rode:
```bash
pip install opencv-contrib-python
```

## Processamento básico de imagens

## Convolução matricial

<img src="https://upload.wikimedia.org/wikipedia/commons/1/19/2D_Convolution_Animation.gif?20130203224852" alt="Imagem" style="display: block; margin: 0 auto; width: 80%;">
<p style="margin-left: 15%">Imagem retirada de <a href="https://commons.wikimedia.org/wiki/File:2D_Convolution_Animation.gif">Wikimedia</a></p>

A operação de convolução é um conceito fundamental em processamento de sinais e visão computacional. Matematicamente, a convolução é definida como a integração de duas funções, em que uma é invertida e deslocada em relação à outra, multiplicando-se as duas funções ponto a ponto e somando os resultados. Essa operação é frequentemente usada para processar sinais e imagens, aplicando um filtro ou máscara para realçar características específicas ou realizar operações de suavização.

No contexto do processamento de imagens digitais, a convolução é aplicada utilizando matrizes. A imagem de entrada é representada por uma matriz bidimensional, em que cada elemento corresponde ao valor de intensidade de um pixel. O filtro, também conhecido como kernel ou máscara, é uma matriz menor que é deslizada sobre a imagem de entrada. Em cada posição da matriz, a convolução é realizada multiplicando-se os elementos da matriz de entrada pelos valores correspondentes do filtro e somando-se os resultados. Esse processo é repetido para todas as posições da imagem, gerando uma nova matriz de saída.

O uso de convolução com matrizes em processamento de imagens oferece uma série de possibilidades. É possível aplicar filtros para realizar suavização, como o filtro de média, que substitui cada pixel pela média dos valores em sua vizinhança. Também é possível aplicar filtros de realce de bordas, como o filtro de Sobel, que destaca as transições de intensidade na imagem. Além disso, a convolução pode ser utilizada para realizar operações de detecção de características, como o uso de filtros de detecção de padrões ou reconhecimento de objetos em imagens. A flexibilidade da operação de convolução permite explorar diferentes máscaras para obter resultados específicos e alcançar uma ampla gama de efeitos e transformações na imagem.

## Filtros convolucionais
