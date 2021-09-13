#include <nlohmann/json.hpp>

void set_nil(nlohmann::json& j) {
    j = nullptr;
}
