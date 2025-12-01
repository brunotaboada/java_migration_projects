from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from agno.os import AgentOS
from agno.team import Team

from agents import (
    CodeAnalyzerAgent,
    MigrationAgent,
    TestGeneratorAgent
)

def create_migration_agentos():
    print("🚀 Initializing Java Migration AgentOS...")
    
    analyzer_wrapper = CodeAnalyzerAgent()
    migration_wrapper = MigrationAgent()
    test_gen_wrapper = TestGeneratorAgent()

    agents = [
        analyzer_wrapper.agent,
        migration_wrapper.agent,
        test_gen_wrapper.agent
    ]

    agent_os = AgentOS(
        agents=agents,
        teams=[Team(
            model=OpenAIChat(
                id='qwen3-coder:480b-cloud',
                api_key='ollama',
                base_url='http://localhost:11434/v1'
            ),
            db=SqliteDb(db_file='agno.db'),
            name="Migration Team",
            add_history_to_context=True,
            members=agents
        )]
    )
    
    print(f"✅ AgentOS initialized with {len(agents)} agents:")
    for agent in agents:
        print(f"   - {agent.name}")
    
    return agent_os

def main():
    from utils import get_config
    config = get_config()
    
    print("\n" + "="*80)
    print("JAVA MIGRATION SYSTEM - AgentOS UI")
    print("="*80 + "\n")
    
    agent_os = create_migration_agentos()
    
    app = agent_os.get_app()
    
    port = config.get_ui_port()
    
    print("\n" + "="*80)
    print("📊 AgentOS UI Available")
    print("="*80)
    print(f"\nModel: {config.get_model_name()}")
    print(f"\nAccess the UI at:")
    print(f"   🌐 http://localhost:{port}")
    print("\nAvailable Agents:")
    print("   1. Report Manager - Planning & guidance")
    print("   2. Code Analyzer - Legacy code analysis")
    print("   3. Migration Specialist - Modernization expert")
    print("   4. Test Generator - BDD & unit testing")
    print("   5. QA Specialist - Quality assurance")
    print("\n💬 What You Can Do:")
    print("   ✓ Ask migration strategy questions")
    print("   ✓ Get expert advice from specialists")
    print("   ✓ Learn about the migration process")
    print("   ✓ Plan your migration approach")
    print("   ✓ Understand what each agent does")
    print("\n🚀 To Execute Migrations:")
    print("   After planning in UI, run:")
    print("   • python migrate_java_app.py -i (interactive)")
    print("   • python migrate_java_app.py -s ./source -t ./target")
    print("\n💡 Example Questions to Ask:")
    print("   • 'How should I plan my Java migration?'")
    print("   • 'What modernization level should I choose?'")
    print("   • 'What will happen during migration?'")
    print("   • 'How do you preserve business logic?'")
    print("="*80 + "\n")
    
    return app

if __name__ == "__main__":
    app = main()
    
    print("Starting AgentOS server...")
    print("Press Ctrl+C to stop\n")
    
    try:
        import uvicorn
        from utils import get_config
        
        config = get_config()
        host = config.get_ui_host()
        port = config.get_ui_port()
        
        print(f"Using model: {config.get_model_name()}")
        
        uvicorn.run(app, host=host, port=port)
    except ImportError:
        print("⚠️  uvicorn not installed. Install with: pip install uvicorn")
        print("Or run AgentOS using its built-in server method")
    except Exception as e:
        print(f"❌ Error starting server: {str(e)}")
        print("Tip: Make sure config.yml exists and PyYAML is installed")