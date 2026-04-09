def display6():
    code = '''import numpy as np
def pr(links,num_pages,iterations,damping=0.85):
    ranks=np.ones(num_pages)/num_pages
    M=np.zeros((num_pages,num_pages))
    for page,outgoing_links in links.items():
        if outgoing_links:
            for link in outgoing_links:
                if 0<=link < num_pages:
                    M[link,page]=1/len(outgoing_links)
                else:
                    print(f"Warning:ignoring invalid link {link} from page {page}")
        else:
            M[:,page]=1/num_pages
    M=damping*M+(1-damping)/num_pages
    print("Iteration Results:")
    for i in range(iterations):
        new_ranks=np.dot(M,ranks)
        print(f"Iteration {i+1}:{new_ranks}")
        ranks=new_ranks
    return ranks
if __name__=="__main__":
    num_pages=int(input("Enter the number of pages:"))
    iterations=int(input("Enter the number of iterations:"))
    web_graph={}
    for i in range(num_pages):
        links=list(map(int,input(f"Enter outgoing links from page{i}  (sapce-separated):").split()))
        web_graph[i]=[link for link in links if 0<=link <num_pages]
    ranks=pr(web_graph,num_pages,iterations)
    for i,rank in enumerate(ranks):
        print(f"Final Rank Page{i},{rank:.4f}")'''
    print(code)
