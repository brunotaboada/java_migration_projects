"""
Code Analysis Visualizer

A utility for generating visual elements (tables, charts, graphs) for code analysis reports.
Supports markdown-formatted tables and ASCII-based charts for better readability.
"""

from dataclasses import dataclass
from typing import Dict, List, Any


@dataclass
class ChartData:
    """Data structure for chart generation"""
    title: str
    data: List[Dict[str, Any]]
    chart_type: str  # 'bar', 'pie', 'table', 'grid'
    unit: str = ""
    max_items: int = 10


class CodeAnalysisVisualizer:
    
    def __init__(self):
        self.visualization_cache = {}
    
    def generate_project_structure_chart(self, structure_data: Dict[str, Any]) -> str:
        """Generate visual representation of project structure"""
        chart = []
        chart.append("# Project Structure Visualization")
        chart.append("")
        
        # File type distribution table
        chart.append("## File Type Distribution")
        file_stats = self._get_file_type_stats(structure_data)
        chart.append(self._generate_table(
            ["File Type", "Count", "Percentage"],
            [[k, str(v['count']), f"{v['percentage']:.1f}%"] for k, v in file_stats.items()]
        ))
        chart.append("")
        
        # Directory tree visualization
        chart.append("## Directory Tree")
        tree = self._generate_directory_tree(structure_data)
        chart.append("```")
        chart.append(tree)
        chart.append("```")
        chart.append("")
        
        # Summary statistics
        chart.append("## Summary Statistics")
        total_files = sum(f['count'] for f in file_stats.values())
        total_dirs = len(structure_data.get('directories', []))
        chart.append(f"- **Total Files**: {total_files}")
        chart.append(f"- **Total Directories**: {total_dirs}")
        chart.append(f"- **Java Files**: {file_stats.get('java', {'count': 0})['count']}")
        chart.append(f"- **Config Files**: {file_stats.get('config', {'count': 0})['count']}")
        
        return "\n".join(chart)
    
    def generate_dependencies_table(self, dependencies_data: Dict[str, Any]) -> str:
        """Generate formatted dependencies table"""
        table = []
        table.append("# Dependencies Analysis")
        table.append("")
        
        imports = dependencies_data.get('imports', [])
        
        # Categorize imports
        categorized = self._categorize_imports(imports)
        
        if categorized['external']:
            table.append("## External Dependencies")
            table.append(self._generate_table(
                ["Package", "Library Type", "Usage"],
                [[imp, self._get_import_category(imp), self._get_import_usage(imp)] 
                 for imp in categorized['external'][:15]]
            ))
            table.append("")
        
        if categorized['internal']:
            table.append("## Internal Dependencies")
            table.append(self._generate_table(
                ["Package", "Module", "Type"],
                [[imp, self._extract_module_name(imp), self._get_import_category(imp)] 
                 for imp in categorized['internal'][:10]]
            ))
            table.append("")
        
        # Dependencies by category chart
        if categorized['external'] or categorized['internal']:
            table.append("## Dependency Distribution")
            categories = {
                'Java Standard Library': len([imp for imp in imports if imp.startswith('java.')]),
                'External Libraries': len(categorized['external']),
                'Internal Modules': len(categorized['internal'])
            }
            table.append(self._generate_bar_chart(categories, "Dependency Types"))
            table.append("")
        
        return "\n".join(table)
    
    def generate_quality_metrics_table(self, quality_data: Dict[str, Any]) -> str:
        """Generate code quality metrics visualization"""
        table = []
        table.append("# Code Quality Metrics")
        table.append("")
        
        # Quality summary table
        quality_summary = self._extract_quality_summary(quality_data)
        if quality_summary:
            table.append("## Quality Assessment Summary")
            table.append(self._generate_table(
                ["Metric", "Rating", "Status", "Priority"],
                [[metric, data['rating'], data['status'], data['priority']] 
                 for metric, data in quality_summary.items()]
            ))
            table.append("")
        
        # Code issues breakdown
        issues = self._extract_issues_list(quality_data)
        if issues:
            table.append("## Code Issues Breakdown")
            severity_counts = self._count_issues_by_severity(issues)
            table.append(self._generate_bar_chart(severity_counts, "Issues by Severity"))
            table.append("")
            
            # Top issues table
            table.append("## Critical Issues")
            critical_issues = [issue for issue in issues if issue.get('severity') == 'HIGH'][:5]
            if critical_issues:
                table.append(self._generate_table(
                    ["Issue Type", "Severity", "Location", "Risk"],
                    [[issue['type'], issue['severity'], 
                      self._format_location(issue.get('locations', [])), 
                      issue.get('risk', 'Unknown')] 
                     for issue in critical_issues]
                ))
                table.append("")
        
        return "\n".join(table)
    
    def generate_business_logic_table(self, business_data: Dict[str, Any]) -> str:
        """Generate business logic analysis table"""
        table = []
        table.append("# Business Logic Analysis")
        table.append("")
        
        business_rules = self._extract_business_rules(business_data)
        if business_rules:
            table.append("## Business Rules Inventory")
            table.append(self._generate_table(
                ["Rule ID", "Description", "Location", "Complexity", "Priority"],
                [[rule.get('rule_id', rule.get('id', 'N/A')), 
                  rule.get('description', rule.get('name', 'Unknown'))[:50] + "...", 
                  self._format_business_location(rule), 
                  rule.get('complexity', 'Unknown'), 
                  rule.get('migration_priority', rule.get('priority', 'Unknown'))] 
                 for rule in business_rules[:10]]
            ))
            table.append("")
        
        # Complexity distribution
        if business_rules:
            complexity_dist = self._count_by_field(business_rules, 'complexity')
            if complexity_dist:
                table.append("## Business Logic Complexity")
                table.append(self._generate_pie_chart(complexity_dist, "Complexity Distribution"))
                table.append("")
        
        return "\n".join(table)
    
    def generate_migration_complexity_chart(self, complexity_data: Dict[str, Any]) -> str:
        """Generate migration complexity visualization"""
        chart = []
        chart.append("# Migration Complexity Assessment")
        chart.append("")
        
        # Overall complexity rating
        overall = self._extract_overall_complexity(complexity_data)
        if overall:
            chart.append("## Overall Complexity Rating")
            chart.append(f"**Rating**: {overall.get('rating', 'Unknown')}")
            chart.append(f"**Score**: {overall.get('score', 'Unknown')}")
            chart.append(f"**Justification**: {overall.get('justification', 'No description available')}")
            chart.append("")
        
        # Complexity factors breakdown
        factors = self._extract_complexity_factors(complexity_data)
        if factors:
            chart.append("## Complexity Factors")
            factor_table = []
            for category, data in factors.items():
                if isinstance(data, dict):
                    rating = data.get('rating', 'Unknown')
                    factor_table.append([category, rating, data.get('impact', 'No impact info')])
            
            if factor_table:
                chart.append(self._generate_table(
                    ["Factor Category", "Rating", "Impact"],
                    factor_table
                ))
                chart.append("")
        
        # Risk assessment
        risks = self._extract_risk_assessment(complexity_data)
        if risks:
            chart.append("## Risk Assessment")
            risk_chart_data = {risk['area']: risk['risk_level'] for risk in risks[:5]}
            chart.append(self._generate_table(
                ["Area", "Risk Level", "Description", "Mitigation"],
                [[risk['area'], risk['risk_level'], risk.get('description', 'No description')[:50] + "...", 
                  risk.get('mitigation', 'No mitigation plan')[:30] + "..."] 
                 for risk in risks[:5]]
            ))
            chart.append("")
        
        return "\n".join(chart)
    
    def _generate_table(self, headers: List[str], data: List[List[str]]) -> str:
        """Generate a markdown table"""
        if not headers or not data:
            return ""
        
        # Calculate column widths
        col_widths = [len(header) for header in headers]
        for row in data:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))
        
        # Generate table
        table = []
        
        # Header row
        header_row = "| " + " | ".join(headers[i].ljust(col_widths[i]) for i in range(len(headers))) + " |"
        separator = "|" + "|".join("-" * (width + 2) for width in col_widths) + "|"
        
        table.append(header_row)
        table.append(separator)
        
        # Data rows
        for row in data:
            data_row = "| " + " | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))) + " |"
            table.append(data_row)
        
        return "\n".join(table)
    
    def _generate_bar_chart(self, data: Dict[str, Any], title: str) -> str:
        """Generate ASCII bar chart"""
        if not data:
            return ""
        
        chart = [f"### {title}", ""]
        
        # Scale for visualization
        max_value = max(data.values()) if data.values() else 1
        chart_width = 30
        
        for label, value in sorted(data.items(), key=lambda x: x[1], reverse=True):
            if max_value == 0:
                bar = ""
            else:
                bar_length = int((value / max_value) * chart_width)
                bar = "█" * bar_length
            
            chart.append(f"{label[:20]:20} |{bar:<30} | {value}")
        
        chart.append("")
        return "\n".join(chart)
    
    def _generate_pie_chart(self, data: Dict[str, Any], title: str) -> str:
        """Generate ASCII pie chart representation"""
        if not data:
            return ""
        
        chart = [f"### {title}", ""]
        
        total = sum(data.values())
        if total == 0:
            chart.append("No data available")
            return "\n".join(chart)
        
        # Simple pie chart using text representation
        for label, value in data.items():
            percentage = (value / total) * 100
            bar_length = int(percentage / 5)  # 20 chars max
            bar = "█" * bar_length
            chart.append(f"{label[:15]:15} [{bar:<20}] {percentage:5.1f}% ({value})")
        
        chart.append("")
        return "\n".join(chart)
    
    def _generate_directory_tree(self, structure: Dict[str, Any]) -> str:
        """Generate directory tree visualization"""
        lines = []
        
        def add_tree(items, prefix="", is_last=True):
            connector = "└── " if is_last else "├── "
            lines.append(f"{prefix}{connector}{items['name']}")
            
            if 'children' in items:
                children = items['children']
                for i, child in enumerate(children):
                    is_last_child = i == len(children) - 1
                    new_prefix = prefix + ("    " if is_last else "│   ")
                    add_tree(child, new_prefix, is_last_child)
        
        # Build tree structure
        tree_data = self._build_tree_structure(structure)
        if tree_data:
            for i, item in enumerate(tree_data):
                is_last = i == len(tree_data) - 1
                add_tree(item, "", is_last)
        
        return "\n".join(lines)
    
    def _build_tree_structure(self, structure: Dict[str, Any]) -> List[Dict]:
        """Build tree structure from flat directory list"""
        tree = []
        directories = structure.get('directories', [])
        
        # Sort directories by depth
        directories.sort(key=lambda d: d.count('/'))
        
        for directory in directories:
            parts = directory.split('/')
            tree.append({'name': parts[-1] if parts else directory, 'children': []})
        
        return tree
    
    def _get_file_type_stats(self, structure: Dict[str, Any]) -> Dict[str, Dict]:
        """Get file type statistics"""
        stats = {
            'java': {'count': len(structure.get('java_files', [])), 'percentage': 0},
            'config': {'count': len(structure.get('config_files', [])), 'percentage': 0},
            'other': {'count': len(structure.get('other_files', [])), 'percentage': 0}
        }
        
        total = sum(stats[k]['count'] for k in stats)
        if total > 0:
            for key in stats:
                stats[key]['percentage'] = (stats[key]['count'] / total) * 100
        
        return stats
    
    def _categorize_imports(self, imports: List[str]) -> Dict[str, List[str]]:
        """Categorize imports into external, internal, etc."""
        categorized = {
            'external': [],
            'internal': [],
            'standard': []
        }
        
        for imp in imports:
            if imp.startswith('java.') or imp.startswith('javax.'):
                categorized['standard'].append(imp)
            elif imp.startswith('com.example.') or imp.startswith('com.') or imp.startswith('org.'):
                categorized['external'].append(imp)
            else:
                categorized['internal'].append(imp)
        
        return categorized
    
    def _get_import_category(self, import_stmt: str) -> str:
        """Categorize import statement"""
        if import_stmt.startswith('java.') or import_stmt.startswith('javax.'):
            return "Standard Library"
        elif '.' in import_stmt:
            return "External Library"
        else:
            return "Internal"
    
    def _get_import_usage(self, import_stmt: str) -> str:
        """Estimate import usage type"""
        if 'util' in import_stmt.lower():
            return "Utility"
        elif 'io' in import_stmt.lower():
            return "I/O"
        elif 'net' in import_stmt.lower():
            return "Network"
        else:
            return "General"
    
    def _extract_module_name(self, import_stmt: str) -> str:
        """Extract module name from import statement"""
        parts = import_stmt.split('.')
        return parts[1] if len(parts) > 1 else import_stmt
    
    def _extract_quality_summary(self, quality_data: Dict[str, Any]) -> Dict[str, Dict]:
        """Extract quality metrics summary from analysis data"""
        summary = {}
        
        # This would parse the JSON structure from the analysis
        # For now, return empty - needs to be implemented based on actual data structure
        return summary
    
    def _extract_issues_list(self, quality_data: Dict[str, Any]) -> List[Dict]:
        """Extract list of issues from quality data"""
        # This would parse the JSON structure from the analysis
        # For now, return empty - needs to be implemented based on actual data structure
        return []
    
    def _count_issues_by_severity(self, issues: List[Dict]) -> Dict[str, int]:
        """Count issues by severity level"""
        counts = {}
        for issue in issues:
            severity = issue.get('severity', 'Unknown')
            counts[severity] = counts.get(severity, 0) + 1
        return counts
    
    def _extract_business_rules(self, business_data: Dict[str, Any]) -> List[Dict]:
        """Extract business rules from business logic data"""
        # This would parse the JSON structure from the business logic analysis
        # For now, return empty - needs to be implemented based on actual data structure
        return []
    
    def _count_by_field(self, data: List[Dict], field: str) -> Dict[str, int]:
        """Count items by a specific field value"""
        counts = {}
        for item in data:
            value = item.get(field, 'Unknown')
            counts[value] = counts.get(value, 0) + 1
        return counts
    
    def _format_location(self, locations: List[str]) -> str:
        """Format location information"""
        if not locations:
            return "Unknown"
        return locations[0][:30] + "..." if len(locations[0]) > 30 else locations[0]
    
    def _format_business_location(self, rule: Dict) -> str:
        """Format business rule location"""
        location = rule.get('location', rule.get('method', 'Unknown'))
        return location[:40] + "..." if len(location) > 40 else location
    
    def _extract_overall_complexity(self, complexity_data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract overall complexity rating from data"""
        # This would parse the JSON structure from complexity assessment
        # For now, return empty - needs to be implemented based on actual data structure
        return {}
    
    def _extract_complexity_factors(self, complexity_data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract complexity factors from data"""
        # This would parse the JSON structure from complexity assessment
        # For now, return empty - needs to be implemented based on actual data structure
        return {}
    
    def _extract_risk_assessment(self, complexity_data: Dict[str, Any]) -> List[Dict]:
        """Extract risk assessment from data"""
        # This would parse the JSON structure from complexity assessment
        # For now, return empty - needs to be implemented based on actual data structure
        return []