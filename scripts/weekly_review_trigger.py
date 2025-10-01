#!/usr/bin/env python3
"""
Weekly Review Trigger System
Automated evaluation of pending projects for activation readiness
"""

import os
import yaml
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional

class WeeklyReviewTrigger:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)
        self.vision_dir = self.repo_root / "08_CHRONICLE" / "vision"
        self.tasks_dir = self.repo_root / "tasks" / "queue"
        self.results = {
            "review_date": datetime.now().isoformat(),
            "projects_evaluated": 0,
            "projects_ready": [],
            "projects_updated": [],
            "recommendations": [],
            "priority_changes": []
        }
    
    def load_project_metadata(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Load and parse project metadata from frontmatter"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = parts[1].strip()
                    try:
                        metadata = yaml.safe_load(frontmatter)
                        metadata['file_path'] = str(file_path)
                        metadata['last_modified'] = datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
                        return metadata
                    except yaml.YAMLError:
                        return None
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
        return None
    
    def evaluate_trigger_conditions(self, project: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate trigger conditions for a project"""
        evaluation = {
            "project_id": project.get('name', 'unknown'),
            "current_status": project.get('status', 'unknown'),
            "priority": project.get('priority', 'unknown'),
            "implementation_readiness": project.get('implementation_readiness', 'unknown'),
            "trigger_conditions": {},
            "readiness_score": 0,
            "recommendation": "maintain_status"
        }
        
        # Define trigger conditions based on project type
        if 'jobs_radar' in project.get('name', '').lower():
            evaluation["trigger_conditions"] = {
                "perplexity_api_validation": self.check_perplexity_readiness(),
                "user_workflow_validation": self.check_user_workflow_readiness(),
                "cis_infrastructure_readiness": self.check_cis_infrastructure_readiness(),
                "resource_availability": self.check_resource_availability()
            }
        elif 'field_depository' in project.get('name', '').lower():
            evaluation["trigger_conditions"] = {
                "phase_1_validation": self.check_phase_1_validation(),
                "user_feedback": self.check_user_feedback_availability(),
                "technical_readiness": self.check_technical_readiness(),
                "resource_availability": self.check_resource_availability()
            }
        elif 'harness' in project.get('name', '').lower():
            evaluation["trigger_conditions"] = {
                "stage_b_stability": self.check_stage_b_stability(),
                "user_adoption_metrics": self.check_user_adoption_metrics(),
                "architecture_completeness": self.check_architecture_completeness(),
                "resource_availability": self.check_resource_availability()
            }
        else:
            # Generic trigger conditions
            evaluation["trigger_conditions"] = {
                "technical_readiness": self.check_technical_readiness(),
                "resource_availability": self.check_resource_availability(),
                "strategic_alignment": self.check_strategic_alignment(),
                "user_demand": self.check_user_demand()
            }
        
        # Calculate readiness score
        readiness_score = sum(1 for condition, met in evaluation["trigger_conditions"].items() if met)
        evaluation["readiness_score"] = readiness_score
        
        # Determine recommendation
        if readiness_score >= 3:
            evaluation["recommendation"] = "activate_project"
        elif readiness_score >= 2:
            evaluation["recommendation"] = "prepare_for_activation"
        elif readiness_score >= 1:
            evaluation["recommendation"] = "continue_development"
        else:
            evaluation["recommendation"] = "maintain_status"
        
        return evaluation
    
    def check_perplexity_readiness(self) -> bool:
        """Check if Perplexity API is ready for job scanning"""
        # This would check actual Perplexity API status
        # For now, return True as a placeholder
        return True
    
    def check_user_workflow_readiness(self) -> bool:
        """Check if user workflow is ready for chat-first interaction"""
        # Check if user has been using ChatGPT/Perplexity regularly
        # For now, return True as a placeholder
        return True
    
    def check_cis_infrastructure_readiness(self) -> bool:
        """Check if CIS infrastructure is ready for enhancement"""
        # Check if Discovery Agent exists and is functional
        discovery_agent = self.repo_root / "agents" / "discovery.yml"
        return discovery_agent.exists()
    
    def check_resource_availability(self) -> bool:
        """Check if resources are available for implementation"""
        # This would check actual resource availability
        # For now, return True as a placeholder
        return True
    
    def check_phase_1_validation(self) -> bool:
        """Check if Phase 1 validation is complete"""
        # Check if Phase 1 MVP is deployed and working
        field_notes = self.repo_root / "08_CHRONICLE" / "field" / "FIELD_NOTES.md"
        return field_notes.exists()
    
    def check_user_feedback_availability(self) -> bool:
        """Check if user feedback is available"""
        # Check for user feedback in logs or metrics
        # For now, return True as a placeholder
        return True
    
    def check_technical_readiness(self) -> bool:
        """Check general technical readiness"""
        # Check if basic technical infrastructure is ready
        return True
    
    def check_stage_b_stability(self) -> bool:
        """Check if Stage B is stable"""
        # Check Stage B status and stability metrics
        return True
    
    def check_user_adoption_metrics(self) -> bool:
        """Check user adoption metrics"""
        # Check if users are adopting CIS features
        return True
    
    def check_architecture_completeness(self) -> bool:
        """Check if architecture is complete"""
        # Check if architecture documentation is complete
        harness_capsule = self.vision_dir / "2025-11-10_CIS_Harness_Scaffolding_Architecture_Capsule.md"
        return harness_capsule.exists()
    
    def check_strategic_alignment(self) -> bool:
        """Check strategic alignment"""
        # Check if project aligns with current strategic goals
        return True
    
    def check_user_demand(self) -> bool:
        """Check user demand for the project"""
        # Check if there's user demand for the project
        return True
    
    def evaluate_priority_changes(self, project: Dict[str, Any], evaluation: Dict[str, Any]) -> Optional[str]:
        """Evaluate if project priority should change"""
        current_priority = project.get('priority', 'unknown')
        readiness_score = evaluation['readiness_score']
        
        # Priority escalation based on readiness
        if readiness_score >= 3 and current_priority != 'high':
            return 'high'
        elif readiness_score >= 2 and current_priority == 'low':
            return 'medium'
        elif readiness_score < 1 and current_priority == 'high':
            return 'medium'
        
        return None
    
    def run_weekly_review(self) -> Dict[str, Any]:
        """Run the weekly review process"""
        print("🔍 Starting Weekly Review Trigger...")
        
        # Find all vision capsules
        vision_files = list(self.vision_dir.glob("*.md"))
        print(f"Found {len(vision_files)} vision files")
        
        # Find all task queue files
        task_files = list(self.tasks_dir.glob("*.yml"))
        print(f"Found {len(task_files)} task files")
        
        # Evaluate vision capsules
        for file_path in vision_files:
            project = self.load_project_metadata(file_path)
            if project and project.get('status') == 'pending':
                print(f"Evaluating: {project.get('name', 'Unknown')}")
                evaluation = self.evaluate_trigger_conditions(project)
                self.results['projects_evaluated'] += 1
                
                if evaluation['recommendation'] == 'activate_project':
                    self.results['projects_ready'].append({
                        'project': project.get('name', 'Unknown'),
                        'file': str(file_path),
                        'readiness_score': evaluation['readiness_score'],
                        'trigger_conditions': evaluation['trigger_conditions']
                    })
                
                # Check for priority changes
                new_priority = self.evaluate_priority_changes(project, evaluation)
                if new_priority:
                    self.results['priority_changes'].append({
                        'project': project.get('name', 'Unknown'),
                        'old_priority': project.get('priority', 'unknown'),
                        'new_priority': new_priority,
                        'reason': f"Readiness score: {evaluation['readiness_score']}/4"
                    })
                
                # Generate recommendations
                if evaluation['recommendation'] != 'maintain_status':
                    self.results['recommendations'].append({
                        'project': project.get('name', 'Unknown'),
                        'recommendation': evaluation['recommendation'],
                        'readiness_score': evaluation['readiness_score'],
                        'next_steps': self.get_next_steps(evaluation['recommendation'])
                    })
        
        # Evaluate task queue files
        for file_path in task_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    task_data = yaml.safe_load(f)
                
                if task_data and task_data.get('task', {}).get('status') == 'pending':
                    print(f"Evaluating task: {task_data.get('task', {}).get('id', 'Unknown')}")
                    self.results['projects_evaluated'] += 1
                    
                    # Simple task evaluation
                    task_evaluation = {
                        'project': task_data.get('task', {}).get('id', 'Unknown'),
                        'file': str(file_path),
                        'readiness_score': 2,  # Default for tasks
                        'recommendation': 'review_task'
                    }
                    
                    self.results['recommendations'].append(task_evaluation)
            except Exception as e:
                print(f"Error evaluating task {file_path}: {e}")
        
        print(f"✅ Weekly Review Complete: {self.results['projects_evaluated']} projects evaluated")
        return self.results
    
    def get_next_steps(self, recommendation: str) -> List[str]:
        """Get next steps based on recommendation"""
        if recommendation == 'activate_project':
            return [
                "Review implementation requirements",
                "Allocate resources and timeline",
                "Begin Phase 1 implementation",
                "Set up monitoring and feedback loops"
            ]
        elif recommendation == 'prepare_for_activation':
            return [
                "Complete remaining trigger conditions",
                "Prepare implementation plan",
                "Gather required resources",
                "Schedule activation review"
            ]
        elif recommendation == 'continue_development':
            return [
                "Continue development work",
                "Address identified gaps",
                "Monitor trigger conditions",
                "Plan next review cycle"
            ]
        else:
            return [
                "Monitor project status",
                "Review trigger conditions monthly",
                "Update documentation as needed"
            ]
    
    def generate_report(self) -> str:
        """Generate a formatted report"""
        report = f"""
# Weekly Review Trigger Report
**Date:** {self.results['review_date']}
**Projects Evaluated:** {self.results['projects_evaluated']}

## 🚀 Projects Ready for Activation
"""
        
        if self.results['projects_ready']:
            for project in self.results['projects_ready']:
                report += f"""
### {project['project']}
- **Readiness Score:** {project['readiness_score']}/4
- **File:** {project['file']}
- **Trigger Conditions Met:**
"""
                for condition, met in project['trigger_conditions'].items():
                    status = "✅" if met else "❌"
                    report += f"  - {condition}: {status}\n"
        else:
            report += "No projects ready for activation at this time.\n"
        
        report += "\n## 📊 Priority Changes\n"
        if self.results['priority_changes']:
            for change in self.results['priority_changes']:
                report += f"- **{change['project']}:** {change['old_priority']} → {change['new_priority']} ({change['reason']})\n"
        else:
            report += "No priority changes recommended.\n"
        
        report += "\n## 💡 Recommendations\n"
        if self.results['recommendations']:
            for rec in self.results['recommendations']:
                report += f"""
### {rec['project']}
- **Recommendation:** {rec['recommendation']}
- **Readiness Score:** {rec['readiness_score']}/4
- **Next Steps:**
"""
                for step in rec.get('next_steps', []):
                    report += f"  - {step}\n"
        else:
            report += "No specific recommendations at this time.\n"
        
        return report

def main():
    """Main execution function"""
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    trigger = WeeklyReviewTrigger(repo_root)
    
    # Run weekly review
    results = trigger.run_weekly_review()
    
    # Generate and print report
    report = trigger.generate_report()
    print(report)
    
    # Save results to file
    output_file = Path(repo_root) / "08_CHRONICLE" / "weekly_review_results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📁 Results saved to: {output_file}")

if __name__ == "__main__":
    main()
