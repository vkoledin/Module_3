import os
import csv


election_data_csv = os.path.join("Recousres/election_data.csv")
election_analysis_txt = os.path.join("election_analysis.txt") 

total_votes = 0
candidate_votes = {}


with open(election_data_csv, 'r') as election_file:
    csv_reader = csv.DictReader(election_file)
    for row in csv_reader:
        total_votes = total_votes + 1
        candidate_name = row["Candidate"]
        candidate_votes[candidate_name] = candidate_votes.get(candidate_name, 0) + 1


winner = max(candidate_votes, key=candidate_votes.get)


with open(election_analysis_txt, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    
    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")