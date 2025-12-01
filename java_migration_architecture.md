# Java Migration Architecture v2.0

## System Overview

This document describes the multi-agent system for modernizing legacy Java applications, built on the Agno AI framework with React-based UI integration.

## Data Flow Architecture

```
Legacy Project          Agent System              Output Artifacts
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│ .java files │────────▶│ Code        │────────▶│ Modernized  │
│ .xml files  │         │ Analyzer    │         │ Java Code   │
│ .jsp files  │         │ Agent       │         │             │
│ .properties │         └─────────────┘         │ Updated     │
└─────────────┘                  │              │ Configs     │
         │                       ▼              │             │
         │              ┌─────────────┐         │ Test Suite  │
         │              │ Migration   │────────▶│             │
         │              │ Specialist  │         │ Migration   │
         │              │ Agent       │         │ Reports     │
         │              └─────────────┘         │             │
         │                       │              └─────────────┘
         │                       ▼
         │              ┌─────────────┐
         └─────────────▶│ Test        │
                        │ Generator   │
                        │ Agent       │
                        └─────────────┘
```

## Core Architecture

### Agent Components

- **Code Analyzer Agent**: Legacy code analysis and structure mapping
- **Migration Specialist Agent**: Java to Java 17+ modernization
- **Test Generator Agent**: BDD and unit test creation
- **Orchestrator**: Workflow coordination and result aggregation

### Technology Stack

**Backend:**
- Agno AI Framework (v2.2.0+) for agent orchestration
- Python for agent implementation
- SQLite database for agent memory
- Ollama LLM integration for AI capabilities

**Frontend:**
- Next.js 15.2.3 with React 18
- TypeScript for type safety
- Tailwind CSS for styling
- Zustand for state management

## Agent Implementation

### Code Analyzer Agent
**File**: `agents/code_analyzer_agent.py`

**Capabilities:**
- Static code analysis with project structure scanning
- Dependency extraction and analysis
- Business logic identification
- Migration complexity assessment
- Enhanced reporting with visualizations

**Key Features:**
- Memory manager for persistent analysis
- JSON-based structured responses
- Integration with code analysis visualizer

### Migration Specialist Agent
**File**: `agents/migration_agent.py`

**Capabilities:**
- Legacy Java to Java 17+ migration
- Spring Framework modernization
- Configuration file updates
- Business logic preservation
- Multi-format migration support

**Migration Rules:**
- Preserve business logic at all costs
- Modern package structure for Spring Boot 3.7+
- JSP to HTML conversion
- XML modernization
- Target: `./modernized_java_project/src/main`

### Orchestrator
**File**: `java_migration_team.py`

**Workflow Phases:**
1. **Analysis**: Code structure and dependency analysis
2. **Migration**: Automated code transformation
3. **Testing**: Comprehensive test suite creation
4. **QA**: Validation and review

## Configuration System

### Global Configuration (`config.yml`)
```yaml
model:
  name: "qwen3-coder:480b-cloud"
  api_key: "ollama"
  base_url: "http://localhost:11434/v1"

database:
  file: "agno.db"

migration:
  default_java_version: "17"
  default_modernization_level: "high"
  default_coverage_target: 80

ui:
  port: 7777
  host: "0.0.0.0"
```

### Agent Configuration
Each agent has dedicated configuration in `agents_config/{agent_name}/config.yml` with:
- Identity management and role enforcement
- Externalized prompt templates
- System messages for guidance
- Priming configuration for initialization

## React UI Architecture

### Component Structure
```
src/
├── app/page.tsx              # Main application entry
├── components/
│   ├── chat/
│   │   ├── ChatArea/         # Main chat interface
│   │   ├── Sidebar/          # Agent selection
│   │   └── Messages/         # Message handling
│   └── ui/                   # Reusable components
├── hooks/                    # Custom React hooks
├── lib/                      # Utility functions
└── types/                    # TypeScript definitions
```

### Key Features
- Real-time chat interface with agents
- Session management for conversation history
- Multi-media support (images, audio, video)
- Responsive design with dark/light themes

## Migration Workflow

### Phase 1: Project Analysis
```python
team = JavaMigrationTeam(source_path, target_path)
analysis_results = team.code_analyzer.analyze_project_structure(source_path)
```
- Directory structure scanning
- Java file identification and classification
- Configuration file detection
- Dependency extraction

### Phase 2: Code Migration
```python
for file_path, file_info in analysis_results['files'].items():
    team.migration_agent.migrate_java_class(file_path, file_info)
```
- Apply modernization rules
- Transform code to Java 17+ patterns
- Update configurations
- Preserve business logic

### Phase 3: Test Generation
```python
team.test_generator.generate_bdd_scenarios()
team.test_generator.generate_unit_tests()
```
- Create BDD scenarios for business logic
- Generate unit tests for all methods
- Ensure comprehensive coverage
- Create integration tests

### Phase 4: Quality Assurance
- Validate migration completeness
- Verify business logic preservation
- Check test coverage
- Generate quality reports

## Deployment

### Development Setup
```bash
# Backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Frontend
cd agent-ui
npm install
npm run dev

# AgentOS server
python java_migration_agentos.py
```

### Production Deployment
- Docker containerization support
- Environment variable configuration
- Process management with systemd
- Load balancing for scale
- Monitoring and logging integration

## Key Features

### Business Logic Preservation
- Zero-tolerance policy for business logic changes
- Automated validation at each migration step
- Comprehensive testing to ensure functionality
- Manual review checkpoints for critical components

### Performance Optimizations
- Identity priming for faster agent responses
- Externalized prompts for reusable operations
- Batch processing for multiple files
- Caching of analysis results

### Quality Assurance
- Multi-stage validation process
- Automated test generation with 80% coverage target
- Code quality metrics and reporting
- Migration completeness verification

## Benefits

1. **Automated Coordination**: Self-coordinating agents complete tasks efficiently
2. **Comprehensive Analysis**: Deep understanding of legacy code structure
3. **Quality Assurance**: Multi-level validation and testing
4. **Modern Standards**: Migration to Java 17+ with Spring Boot patterns
5. **Cost-Effective**: Uses local Ollama models for AI processing
6. **Extensible**: Modular design allows for easy customization
7. **Production-Ready**: Comprehensive deployment and monitoring capabilities

## Usage Example

```python
from java_migration_team import JavaMigrationTeam

# Initialize the team
team = JavaMigrationTeam(
    source_path="/path/to/legacy/java/project",
    target_path="/path/to/modernized/project"
)

# Execute migration
team.execute_migration()

# Results available in target_path/migration_reports/
```

This architecture provides a robust, scalable solution for Java application modernization while ensuring code quality and business logic preservation throughout the migration process.