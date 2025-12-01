# AGNO Agentic AI Migration Template

A sample template for creating custom agentic AI migration projects using AGNO (Agentic Orchestration Platform), designed to help developers build their own intelligent migration frameworks for any legacy system or programming language.

## 🚀 Overview

This template provides a foundation for building agentic AI migration frameworks using AGNO. It includes:

- **Code Analysis Agent**: Automated analysis of legacy codebases (any language)
- **Report Manager Agent**: Comprehensive reporting and results synthesis with visualizations
- **Migration Specialist Agent**: Guided migration execution with best practices
- **Test Generator Agent**: Automated test case generation for migrated applications
- **Web Interface**: Modern React-based UI for interacting with migration tools
- **AGNO Integration**: Agentic orchestration framework for building custom agents
- **Multi-Language Support**: Framework designed to work with Java, .NET, COBOL, and other legacy systems

### Concise Modernization Strategy

For effective sequential modernization:
- **Phase Planning**: Break down the project into logical, manageable phases
- **Dependency Mapping**: Create a comprehensive dependency graph to guide the sequence
- **Incremental Validation**: Implement continuous testing at each phase
- **Interface Management**: Maintain stable interfaces between modernized and legacy components
- **Documentation**: Thoroughly document each phase for future reference and troubleshooting

## 📋 Features

- **Modular Agent Architecture**: Easily create and integrate custom migration agents for any technology stack
- **Generic Code Analysis**: Comprehensive AI-powered analysis capabilities for multiple languages
- **Comprehensive Reporting**: Automated generation of detailed migration reports with visualizations
- **Guided Execution Framework**: Step-by-step migration assistance system
- **Test Generation System**: Automated test case creation for any migrated codebase
- **Modern Web Interface**: User-friendly React-based dashboard template
- **Multi-Technology Support**: Framework for handling diverse enterprise applications
- **AGNO Integration**: Built-in support for Agentic Orchestration Network
- **Extensible Architecture**: Designed to support Java, .NET, COBOL, and other legacy systems

## 🛠 Technology Stack

### Backend

- **Python 3.8+**: Core runtime environment
- **FastAPI**: RESTful API framework
- **AGNO Framework**: Agentic orchestration and coordination
- **AI/ML Integration**: Powered by advanced language models
- **Configuration Management**: YAML-based agent configurations
- **Multi-Language Analysis**: Support for Java, .NET, COBOL, and other legacy systems

### Frontend

- **React 18**: Modern UI framework
- **Next.js**: Full-stack React framework
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first styling
- **Shadcn/ui**: High-quality component library

### Universal Analysis

- **Multi-Language Support**: Java, .NET, COBOL, and other legacy systems
- **Static Code Analysis**: Custom analysis tools for various languages
- **Project Structure Analysis**: Support for different build systems (Maven, MSBuild, etc.)
- **Dependency Analysis**: Framework for analyzing project dependencies
- **Report Generation**: Comprehensive reporting system with visualizations

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Node.js 16+ and npm/pnpm
- AGNO Framework (included in requirements)
- Language-specific tools as needed for your target migration projects

### Setup

1. **Clone the template repository**
   ```bash
   git clone <repository-url>
   cd java_migration_projects
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your custom agents**
   ```bash
   # Edit configuration files in agents_config/ directory
   # Create new agent configurations following the template structure
   # Customize for your target languages and systems
   ```

## 🚀 Quick Start

### Running the Framework

1. **Start the AGNO backend server**
   ```bash
   python java_migration_team.py
   ```

2. **Start the frontend development server**
   ```bash
   cd agent-ui
   npm run dev
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - API Documentation: http://localhost:8000/docs
   - AGNO Dashboard: http://localhost:8000/agno

### Basic Usage Template

1. **Upload Legacy Project**: Use the web interface to upload your target project (any language)
2. **Analyze Code**: Let your custom Code Analyzer Agent examine the codebase
3. **Execute Migration**: Follow guided steps with your Migration Specialist Agent
4. **Generate Tests**: Automatically create test cases with your Test Generator Agent
5. **Generate Reports**: Create comprehensive migration reports with the Report Manager Agent
6. **Create Custom Agents**: Build new agents using the AGNO framework for your specific needs
7. **Extend for Your Language**: Customize the framework for Java, .NET, COBOL, or other systems

## 📁 Project Structure

```
java_migration_projects/
├── agent-ui/                 # React frontend application template
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── app/             # Next.js app directory
│   │   ├── lib/             # Utility functions
│   │   └── types/           # TypeScript type definitions
│   ├── package.json
│   └── next.config.ts
├── agents/                  # Core agent implementations (template)
│   ├── code_analyzer_agent.py
│   ├── migration_agent.py
│   ├── migration_planner_agent.py  # Contains ReportAgent implementation
│   ├── test_generator_agent.py
│   └── your_custom_agent.py # Add your custom agents here
├── agents_config/           # Agent configuration files
│   ├── code_analyzer/
│   ├── migration_specialist/
│   ├── report_manager/      # Report Manager configuration
│   ├── test_generator/
│   └── your_custom_agent/   # Add your custom agent configs
├── sample_projects/         # Sample projects for testing (rename from legacy_java_project)
│   ├── java_example/        # Java project example
│   ├── dotnet_example/      # .NET project example (add your own)
│   └── cobol_example/       # COBOL project example (add your own)
└── utils/                   # Utility modules
    ├── agent_config_loader.py
    ├── code_analysis_visualizer.py  # Visualization tools for reports
    └── config_loader.py
```

## 🤝 Creating Custom Agents with AGNO

This template is designed to help you create your own agentic AI migration projects using AGNO for any legacy system or programming language. Here's how to get started:

### Building Your First Custom Agent

1. **Create a new agent file** in the `agents/` directory
2. **Define agent capabilities** using the AGNO framework
3. **Create configuration** in `agents_config/your_agent_name/`
4. **Integrate with the web interface** through the API
5. **Customize for your target language** (Java, .NET, COBOL, etc.)

### Agent Development Guidelines

- Follow the existing agent structure for consistency
- Use AGNO's orchestration capabilities for agent coordination
- Implement proper error handling and logging
- Document your agent's capabilities and limitations
- Design agents to be language-agnostic where possible
- Create language-specific extensions when needed

### Multi-Language Support

The framework is designed to be extended for various legacy systems:

- **Java Migration**: Use the existing Java analysis tools as reference
- **.NET Migration**: Add MSBuild project analysis capabilities
- **COBOL Migration**: Implement COBOL-specific analysis modules
- **Other Languages**: Extend the framework for your specific needs

### Report Manager Agent

The **Report Manager Agent** is a key component that provides:

- **Comprehensive Reporting**: Generates detailed migration reports with executive summaries
- **Results Synthesis**: Combines outputs from all agents into cohesive final reports
- **Visualization Support**: Creates graphs, tables, and visual elements for easy understanding
- **Custom Report Generation**: Can be extended to create language-specific report formats
- **API Integration**: Provides endpoints for report generation and retrieval

The Report Manager Agent is implemented in `agents/migration_planner_agent.py` and uses the configuration in `agents_config/report_manager/`. It can synthesize results from multiple agents and generate comprehensive reports with visualizations using the `code_analysis_visualizer.py` utility.
## 📝 API Documentation

The API documentation is automatically generated and available at `/docs` when running the backend server.

### Key Endpoints Template

- `POST /api/analyze` - Analyze codebase (customizable for any language)
- `POST /api/execute-migration` - Execute migration steps (extendable)
- `POST /api/generate-tests` - Generate test cases (modifiable)
- `POST /api/generate-report` - Generate comprehensive migration reports
- `POST /api/custom-endpoint` - Add your custom endpoints
- `POST /api/language-specific` - Create language-specific analysis endpoints

## 🧪 Testing

### Running Tests

```bash
# Backend tests
pytest

# Frontend tests
cd agent-ui
npm test
```

### Test Structure

- **Unit Tests**: Individual component and function testing
- **Integration Tests**: End-to-end workflow testing
- **API Tests**: RESTful endpoint validation
- **Agent Tests**: Custom agent behavior testing
- **Multi-Language Tests**: Language-specific analysis validation
- **Report Generation Tests**: Validate report quality and completeness

## 📊 Sample Projects

The repository includes sample projects for testing and demonstration:

- **java_example**: Simple Java application template (reference implementation)
- **legacy_java_project2**: Complex multi-module Java EE application example

**Add your own examples for other languages:**
- Create `.NET` project examples in `sample_projects/dotnet_example/`
- Add `COBOL` examples in `sample_projects/cobol_example/`
- Include other legacy system examples as needed

Use these as starting points and templates for your own migration projects across different languages.

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed
2. **Frontend Build Issues**: Clear node_modules and reinstall dependencies
3. **Agent Configuration**: Verify YAML configuration files are valid
4. **AGNO Integration**: Check AGNO framework compatibility
5. **Language-Specific Issues**: Install required tools for your target language
6. **Report Generation**: Ensure visualization dependencies are available

### Getting Help

- Check the [Issues](../../issues) page for known problems
- Review API documentation at `/docs`
- Consult the sample projects for reference implementations
- Explore AGNO framework documentation for advanced features
- Research language-specific migration best practices
- Examine report manager configuration for reporting customization

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](agent-ui/LICENSE) file for details.

### MIT License Summary

```
MIT License

Copyright (c) 2025 AGNO Universal Agentic AI Migration Framework Template

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Acknowledgments

- Thanks to the open source community for the excellent tools and libraries
- Special recognition to the AGNO framework developers
- Inspiration from modern DevOps, CI/CD, and agentic AI best practices
- Appreciation to contributors of multi-language migration tools and techniques

## 👥 Contributors

- [Bruno Taboada (@brunotaboada)](https://github.com/brunotaboada)

## 📞 Support

For support, questions, or feature requests:

1. **Issues**: Open an issue on GitHub
2. **Documentation**: Check the inline code documentation
3. **API Docs**: Visit `/docs` for detailed API information
4. **AGNO Framework**: Consult AGNO documentation for advanced features
5. **Multi-Language Resources**: Research language-specific migration guides
6. **Reporting Features**: Review report manager documentation for customization options

---

**Build Universal Agentic AI Migration Projects with AGNO!** 🌍🚀