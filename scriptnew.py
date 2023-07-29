import math

# HTML Template
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{hz} Hz to Rad/s</title>
    <link rel="icon" href="img/favicon.ico" sizes="any">
    <link rel="icon" href="img/favicon.svg" type="image/svg+xml">
    <link rel="apple-touch-icon" href="img/favicon.png">
    <link rel="canonical" href="{{hz}}hz-to-rads.html">
    <link rel="stylesheet" type="text/css" href="styles.css">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1527675586070314"
     crossorigin="anonymous"></script>
</head>
<body>
  <div class="logo">
      <a href="https://hztorad.com">
        <img src="img/hztorad.png" alt="Logo" width="280">
      </a>
    </div>
    
  <h1>{hz} Hz to Rad/s</h1>
  <div class="container">
    <nav aria-label="breadcrumb">
            <ol class="breadcrumb">
              <li class="breadcrumb-item"><a href="index.html">Home</a></li>
              <li class="breadcrumb-item active" aria-current="page">{hz} Hz to Rad/s </li>
            </ol>
          </nav>

    <p>To convert {hz} Hertz to radians per second, Multiply {hz}Hz by 2π rad. {hz} Hz times 2π rad gives you {rads} rad/s. Therefore, a frequency of {hz} Hz is equivalent to an angular velocity of {rads} rad/s.</p>
    <h2>Formula for {hz} Hz to Rad/s</h2>
    <p>Given a frequency of {hz} Hz, the conversion to radians per second (rad/s) can be expressed as:</p>
    <p>ω = 2π * f</p>
    <p>Where:</p>
    <ul>
        <li>ω is the angular frequency in rad/s,</li>
        <li>π is a mathematical constant approximately equal to 3.14159,</li>
        <li>f is the frequency in Hz.</li>
    </ul>
    <p>Substituting the given frequency into the formula:</p>
    <p>ω = 2π * {hz} Hz</p>
    <p>Therefore,</p>
    <p>ω = {rads} rad/s or {degrees}°/s</p>
    <h2>Hz to Rad/s Converter</h2>
    <div class="calculator-wrapper">
        <div class="calculator">
            <div class="inputGroup">
                <label for="frequency">Hertz (Hz):</label>
                <input type="number" id="frequency" min="0" required>
            </div>
            <div class="buttonGroup">
                <button class="calculator-button" id="calculate">Calculate</button>
                <button class="calculator-button" id="reset">Reset</button>
            </div>
            <div class="inputGroup">
                <label for="result">Result (rad/s):</label>
                <input type="text" id="result" readonly>
            </div>
            <p id="error-message" style="display: none;">Invalid input. Please enter a positive number.</p>
        </div>
    </div>
    <script>
        const frequencyInput = document.getElementById('frequency');
        const resultInput = document.getElementById('result');
        const calculateButton = document.getElementById('calculate');
        const resetButton = document.getElementById('reset');
        const errorMessage = document.getElementById('error-message');
        calculateButton.addEventListener('click', function() {{
          const frequency = parseFloat(frequencyInput.value);
          if (isNaN(frequency) || frequency < 0) {{
            errorMessage.style.display = 'block';
            resultInput.value = '';
          }} else {{
            errorMessage.style.display = 'none';
            resultInput.value = (2 * Math.PI * frequency).toFixed(2) + ' rad/s';
          }}
        }});
        resetButton.addEventListener('click', function() {{
          frequencyInput.value = '';
          resultInput.value = '';
          errorMessage.style.display = 'none';
        }});
    </script>
 <div class="related">

    <h2>Related Articles</h2>
    {related_articles_html}
  </div>
  </div>
  <footer>
    <div class="footer-container">
        <div class="copyright">
            &copy; Hz to Rad/s
        </div>
        <nav>
            <ul>
                <li><a href="Privacy-Policy.html">Privacy Policy</a></li>
                <li><a href="Help.html">Help</a></li>
                <li><a href="contact-us.html">Contact Us</a></li>
            </ul>
        </nav>
    </div>
  </footer>
  
</body>
</html>
"""

related_article = """
    <div class="article-preview">
        <a href="{next_hz}hz-to-rads.html">
          <h3>{next_hz} Hz to Rad/s</h3>
        </a>
        <p>This article explains how to convert a frequency of {next_hz} Hz to radians per second.</p>
    </div>
"""

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for hz in range(start, end+1):
    rads = 2 * math.pi * hz
    degrees = rads * (180 / math.pi)
    
    related_articles_html = ""
    for i in range(1, 5):
        next_hz = hz + i if hz + i <= end else start + i - 1
        related_articles_html += related_article.format(next_hz=next_hz)
    
    # Filling the HTML Template with values
    html = template.format(hz=hz, rads=round(rads, 2), degrees=round(degrees, 2), related_articles_html=related_articles_html)
    
    # Writing the HTML file
    with open(f"{hz}hz-to-rads.html", "w", encoding='utf-8') as file:
        file.write(html)

print("Articles have been generated successfully!")
