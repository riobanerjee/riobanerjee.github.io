#!/usr/bin/env python3
import yaml
import sys
from datetime import datetime

def load_publications(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def generate_latex_publications(publications, output_file, selected_only=False):
    with open(output_file, 'w') as f:
        papers = publications['papers']
        
        # Sort by year (newest first)
        papers.sort(key=lambda x: x['year'], reverse=True)
        
        current_year = None
        for paper in papers:
            # For industry CV, only include selected papers
            if selected_only and not paper.get('selected', False):
                continue
                
            if paper['year'] != current_year:
                if current_year is not None:
                    f.write('\n')
                current_year = paper['year']
                f.write(f'\\subsection{{{current_year}}}\n\n')
            
            # Format the publication entry
            f.write(f'\\cventry{{}}{{{paper["title"]}}}{{{paper["venue"]}}}{{}}{{}}{{\n')
            f.write(f'  {paper["authors"]}\\\\\n')
            
            # Add links
            links = []
            for link_type, url in paper.get('links', {}).items():
                links.append(f'\\href{{{url}}}{{[{link_type.capitalize()}]}}')
            
            if links:
                f.write(f'  {" ".join(links)}\n')
            
            f.write('}\n\n')

if __name__ == "__main__":
    publications = load_publications('_data/publications.yml')
    
    # Generate full publications list for academic CV
    generate_latex_publications(
        publications,
        'cv/academic/sections/publications.tex'
    )
    
    # Generate selected publications for industry CV
    generate_latex_publications(
        publications,
        'cv/industry/sections/publications_selected.tex',
        selected_only=True
    )