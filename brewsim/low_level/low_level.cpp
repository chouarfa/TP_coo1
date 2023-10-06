
#include <iostream>
#include <string>
#include <cpr/cpr.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

class Departement {
public:
    int numero;
    double prix_m2;

    Departement(int num, double prix) : numero(num), prix_m2(prix) {}

    Departement(const json& data) {
        numero = data["numero"].get<int>();
        prix_m2 = data["prix_m2"].get<double>();
    }

    Departement(int id) {
        auto Response = cpr::Get(cpr::Url{"http://localhost:8000/departement/" + std::to_string(id)});
        json data = json::parse(Response.text);
        numero = data["numero"].get<int>();
        prix_m2 =data["prix_m2"].get<double>();
    }

    friend std::ostream& operator<<(std::ostream& out, const Departement& d) {
        return out << d.numero << " / " << d.prix_m2;
    }
};

int main() {
    Departement d{50, 152.2};
    std::cout << d << "\n";

    auto Response = cpr::Get(cpr::Url{"http://localhost:8000/departement/1"});
    std::cout << "La réponse est " << Response.text << std::endl;

    json data = json::parse(Response.text);

    Departement departementFromJSON(data);
    std::cout << "Departement à partir de JSON: " << departementFromJSON << std::endl;

    int id=1;
    Departement departementWithId(id);
    std::cout << "Departement avec un ID : " << departementWithId << std::endl;

    return 0;
}
