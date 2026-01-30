#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>

struct Repo {
    std::string name;
    int stars;
    int forks;
    int issues;
    double score;
};

double compute_score(const Repo& r) {
    return (r.stars * 0.6) + (r.forks * 0.3) - (r.issues * 0.1);
}

int main() {
    std::ifstream file;
    file.open("data/repos.csv");

    if (!file.is_open()) {
        std::cerr << "Failed to open CSV file\n";
        return 1;
    }

    std::string line;
    std::getline(file, line); // skip header

    std::vector<Repo> repos;

    while (std::getline(file, line)) {
        std::stringstream ss(line);
        Repo r;
        std::string token;

        std::getline(ss, r.name, ',');
        std::getline(ss, token, ',');
        r.stars = std::stoi(token);
        std::getline(ss, token, ',');
        r.forks = std::stoi(token);
        std::getline(ss, token, ',');
        r.issues = std::stoi(token);

        r.score = compute_score(r);
        repos.push_back(r);
    }

    std::sort(
        repos.begin(),
        repos.end(),
        [](const Repo& a, const Repo& b) {
            return a.score > b.score;
        }
    );

    std::cout << "\nTop Ranked Repositories\n";
    std::cout << "-----------------------\n";

    for (size_t i = 0; i < repos.size() && i < 10; ++i) {
        std::cout << i + 1 << ". "
                  << repos[i].name
                  << " | score: " << repos[i].score
                  << "\n";
    }

    return 0;
}
