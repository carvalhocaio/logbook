# LogBook 📚

A modern, elegant Django web application for personal journaling and note-taking, featuring a beautiful shadcn/ui-inspired design with advanced filtering capabilities and responsive layouts.

## ✨ Features

### 🎨 Modern UI/UX
- **shadcn/ui Design System**: Beautiful, accessible interface with consistent styling
- **Dark/Light Mode**: System-aware theme with manual toggle and localStorage persistence
- **Responsive Design**: Mobile-first approach with device-specific optimizations
- **Progressive Enhancement**: Core functionality works without JavaScript

### 📱 Mobile-Optimized Experience
- **Desktop**: Static action bars with scroll-to-top functionality
- **Mobile**: Full-width sticky bottom buttons with fade gradients
- **Touch-Friendly**: Proper touch targets and gesture-optimized interactions

### 🔍 Advanced Filtering
- **Multi-Filter Search**: Search across titles and content with real-time results
- **Date Filtering**: Specific date picker + quick ranges (today, week, month)
- **Weekday Filter**: Filter entries by days of the week
- **Smart UI**: Collapsible filter panels with active filter indicators
- **State Preservation**: Filters maintained across pagination and navigation

### 📖 Content Management
- **CRUD Operations**: Full create, read, update, delete functionality
- **Pagination**: Elegant 10-per-page pagination with responsive controls
- **Weekend Highlighting**: Visual distinction for weekend entries
- **Rich Content**: Support for long-form content with truncation

### 🔐 Authentication
- **Custom Login**: Beautiful login page matching the app design
- **Secure Access**: All routes protected with Django's authentication system
- **Smart Redirects**: Automatic redirection for authenticated users

## 🏗️ Architecture

### Tech Stack
- **Backend**: Django 5.1 with class-based views
- **Frontend**: Tailwind CSS + Lucide icons via CDN
- **Database**: SQLite (configurable to PostgreSQL/MySQL)
- **Styling**: CSS custom properties for theming

### Design Patterns

#### Authentication Pattern
```python
class LockedView(LoginRequiredMixin):
    login_url = "login"
```
All views inherit from `LockedView` ensuring consistent authentication requirements.

#### Filtering Pattern
Uses Django Q objects for complex queries:
```python
queryset = queryset.filter(
    Q(title__icontains=search) | Q(content__icontains=search)
)
```

#### Responsive UX Pattern
Different behaviors per device type:
- **Desktop**: Horizontal action bars with scroll-to-top
- **Mobile**: Sticky bottom buttons with full-width design

#### Theme System
CSS custom properties enable seamless dark/light mode:
```css
:root { --primary: 221.2 83.2% 53.3%; }
.dark { --primary: 217.2 91.2% 59.8%; }
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd logbook
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment configuration**
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Database setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Seed sample data** (optional)
   ```bash
   python seed.py
   ```

7. **Run development server**
   ```bash
   make run
   # or
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000` to access the application.

## 🛠️ Development Commands

The project includes a `Makefile` for common development tasks:

```bash
make run      # Start development server
make lint     # Run ruff linting with diff output
make format   # Format code with ruff
```

Additional Django commands:
```bash
python manage.py test                    # Run tests
python manage.py makemigrations         # Create migrations
python manage.py migrate                # Apply migrations
python seed.py                          # Generate sample data
```

## 📁 Project Structure

```
logbook/
├── core/                             # Django project configuration
│   ├── settings.py                   # Main settings with environment config
│   ├── urls.py                       # Root URL configuration
│   └── wsgi.py                       # WSGI application
├── entries/                          # Main application
│   ├── models.py                     # Entry model definition
│   ├── views.py                      # Class-based views with filtering
│   ├── urls.py                       # URL patterns
│   ├── templates/entries/            # HTML templates
│   │   ├── base.html                 # Base template with theme system
│   │   ├── login.html                # Custom login page
│   │   ├── entry_list.html           # Main listing with filters
│   │   ├── entry_detail.html         # Entry detail view
│   │   ├── entry_form.html           # Create/edit form
│   │   └── entry_confirm_delete.html # Delete confirmation
│   └── migrations/                   # Database migrations
├── requirements.txt                  # Python dependencies
├── seed.py                           # Sample data generator
├── Makefile                          # Development commands
├── CLAUDE.md                         # AI assistant guidance
└── README.md                         # Project documentation
```

## 🎨 Design System

### Color Palette
The application uses a sophisticated color system based on shadcn/ui:

- **Primary**: Blue (#3b82f6) - Actions and links
- **Secondary**: Gray variants - Backgrounds and subtle elements  
- **Accent**: Interactive elements and hover states
- **Destructive**: Red - Delete actions and errors
- **Muted**: Subdued text and disabled states

### Typography
- **Headings**: Bold, tracking-tight for clear hierarchy
- **Body**: Optimized for readability across devices
- **UI Text**: Consistent sizing (text-sm) for interface elements

### Spacing & Layout
- **Grid System**: Responsive CSS Grid for entries
- **Consistent Spacing**: Tailwind's spacing scale
- **Card Design**: Elevated cards with subtle shadows and borders

## 🔧 Configuration

### Environment Variables
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (True/False)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_URL`: Database connection string

### Database Configuration
Default SQLite configuration supports development. For production:

```env
DATABASE_URL=postgres://user:pass@localhost/dbname
# or
DATABASE_URL=mysql://user:pass@localhost/dbname
```

## 📝 Usage Examples

### Creating Entries
- Click the "New Entry" button (desktop) or bottom action button (mobile)
- Fill in title and content
- Entries are automatically timestamped

### Filtering Content
- Use the "Filters" button to expand filter options
- Search across titles and content
- Filter by specific dates or date ranges
- Filter by weekday to find patterns
- Combine multiple filters for precise results

### Dark Mode
- Toggle manually using the sun/moon icon
- Respects system preference by default
- Preference persisted in browser localStorage

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Workflow
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run linting: `make lint`
5. Commit changes: `git commit -m "Description"`
6. Push to branch: `git push origin feature-name`
7. Open a Pull Request

### Code Standards
- **Python**: Follow PEP 8, enforced by ruff
- **HTML**: Semantic, accessible markup
- **CSS**: Use Tailwind utilities, avoid custom CSS
- **JavaScript**: Progressive enhancement, vanilla JS preferred

### Areas for Contribution
- 🌐 **Internationalization**: Add multi-language support
- 🔍 **Search**: Enhanced search with highlighting
- 📱 **PWA**: Progressive Web App capabilities
- 🔌 **Integrations**: Export/import features
- 🎨 **Themes**: Additional color schemes

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋‍♂️ Support

- 📧 **Issues**: Use GitHub issues for bug reports
- 💡 **Feature Requests**: Open an issue with the `enhancement` label

---
