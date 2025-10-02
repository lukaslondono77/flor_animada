# 🌸 Flor Animada

A modern, high-performance web application that displays personalized images based on user input. Built with Flask and optimized for GitHub Pages deployment.

## ✨ Features

- **Interactive Name Input**: Enter a name to see a personalized image
- **Smooth Animations**: Beautiful loading animations and transitions
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **High Performance**: Optimized for fast loading with modern CSS and JavaScript
- **GitHub Pages Ready**: Automatically deploys to GitHub Pages

## 🚀 Live Demo

Visit the live application: [Flor Animada on GitHub Pages](https://yourusername.github.io/flor_animada)

## 🛠️ Technology Stack

- **Backend**: Python Flask (for development)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Deployment**: GitHub Pages with GitHub Actions
- **Performance**: Minified CSS, image preloading, optimized animations

## 📁 Project Structure

```
flor_animada/
├── app.py                 # Flask development server
├── index.html            # Static HTML for GitHub Pages
├── static/
│   ├── styles.css        # Main stylesheet
│   ├── styles.min.css    # Minified stylesheet
│   └── images/           # Image assets
├── templates/
│   └── index.html        # Flask template
├── .github/workflows/
│   └── deploy.yml        # GitHub Pages deployment
└── README.md
```

## 🏃‍♂️ Quick Start

### Local Development (Flask)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flor_animada.git
   cd flor_animada
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask development server**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8000`

### GitHub Pages Deployment

The application automatically deploys to GitHub Pages when you push to the main branch. No additional configuration needed!

## 🎨 How It Works

1. **User Input**: Enter one of the supported names (Arturo, Julian, or Gina)
2. **Loading Animation**: A beautiful loading animation plays for 3 seconds
3. **Image Display**: The corresponding image appears with a smooth fade-in effect
4. **Reset**: Click the reset button to start over

## ⚡ Performance Optimizations

- **Image Preloading**: All images are preloaded for instant display
- **Minified CSS**: Reduced file size for faster loading
- **Modern CSS**: Uses CSS Grid, Flexbox, and modern properties
- **Efficient Animations**: Uses `requestAnimationFrame` for smooth animations
- **Responsive Design**: Mobile-first approach with optimized breakpoints

## 🎯 Supported Names

- **Arturo** → Shows Arturo's image
- **Julian** → Shows Julian's image  
- **Gina** → Shows Gina's image

## 🔧 Customization

### Adding New Names

1. Add the image file to `static/images/`
2. Update the `nameToImage` object in `index.html`:
   ```javascript
   const nameToImage = {
       'arturo': 'arturo.jpeg',
       'julian': 'julian.jpeg',
       'gina': 'gina.jpeg',
       'newName': 'newName.jpeg'  // Add your new name here
   };
   ```

### Styling

Edit `static/styles.css` and run the minification process:
```bash
# Basic minification (remove comments and extra spaces)
sed 's/\/\*.*\*\///g; s/  */ /g; s/; /;/g' static/styles.css > static/styles.min.css
```

## 📱 Browser Support

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the beauty of interactive web experiences
- Built with modern web standards and best practices
- Optimized for performance and accessibility

---

**Made with ❤️ and modern web technologies**
