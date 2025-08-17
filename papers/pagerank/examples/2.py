from pagerank import PageRank
import viz

links = [
    ("Home", "Products"),
    ("Home", "About"),
    ("Home", "Blog"),
    ("Products", "Product1"),
    ("Products", "Product2"),
    ("Products", "Home"),  # Back to home
    ("Product1", "Product2"),
    ("Product2", "Product1"),
    ("Product1", "Home"),
    ("About", "Home"),
    ("About", "Contact"),
    ("Blog", "BlogPost1"),
    ("Blog", "BlogPost2"),
    ("Blog", "Home"),
    ("BlogPost1", "BlogPost2"),
    ("BlogPost1", "Products"),  # Blog mentions products
    ("BlogPost1", "Home"),
    ("BlogPost2", "BlogPost1"),
    ("BlogPost2", "About"),
    ("BlogPost2", "Contact"),
    ("Contact", "Home"),
    ("Contact", "About"),
    ("Authority", "Home"),
    ("Authority", "Products"),
]

print("Graph links")
print("-" * 20 + "\n")

for source, target in links:
    print(f"  {source} -> {target}")
    
pr = PageRank(damping_factor=0.85, tolerance=1e-3)
scores = pr.calculate(links)
    
print("\nPageRank Scores:")
print("-" * 20)
    
sorted_pages = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for page, score in sorted_pages:
    print(f"{page}: {score:.6f}")

total_score = sum(scores.values())
print(f"\nTotal PageRank sum: {total_score:.1f}")

viz.visualize_pagerank(links, scores, './img/example_2')


import matplotlib.pyplot as plt
import numpy as np

# Count inbound links for each page
inbound_counts = {}
pages = set()

# Get all pages
for source, target in links:
    pages.add(source)
    pages.add(target)

# Initialize counts
for page in pages:
    inbound_counts[page] = 0

# Count inbound links
for source, target in links:
    inbound_counts[target] += 1

# PageRank scores from your output
pagerank_scores = {
    'Home': 0.239018,
    'About': 0.134919,
    'Product1': 0.129423,
    'Products': 0.104339,
    'Product2': 0.099322,
    'Contact': 0.087900,
    'Blog': 0.082779,
    'BlogPost1': 0.053650,
    'BlogPost2': 0.053650,
    'Authority': 0.015000
}

# Create the plot
pages = list(pagerank_scores.keys())
inbound_links = [inbound_counts[page] for page in pages]
pagerank_values = [pagerank_scores[page] for page in pages]

plt.figure(figsize=(10, 6))
plt.scatter(inbound_links, pagerank_values, s=100, alpha=0.7, color='blue')

# Add labels for each point
for i, page in enumerate(pages):
    plt.annotate(page, (inbound_links[i], pagerank_values[i]), 
                xytext=(5, 5), textcoords='offset points', fontsize=9)

plt.xlabel('Number of Inbound Links')
plt.ylabel('PageRank Score')
plt.title('Inbound Links vs PageRank Scores')
plt.grid(True, alpha=0.3)

# Add trend line
z = np.polyfit(inbound_links, pagerank_values, 1)
p = np.poly1d(z)
plt.plot(inbound_links, p(inbound_links), "r--", alpha=0.8, label=f'Trend line')

plt.legend()
plt.tight_layout()
plt.show()

# save the plot
plt.savefig('./img/example_2_plot.png')