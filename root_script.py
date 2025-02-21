import github_script
import organize_script


if __name__ == "__main__":
    organize_script.organize_solutions()
    github_script.generate_readme()
    github_script.git_push()