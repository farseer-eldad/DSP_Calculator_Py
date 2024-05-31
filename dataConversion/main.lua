local dspData = require("recipeData")

local game_recipes = dspData.game_recipes
local game_items = dspData.game_items

for i,v in ipairs(game_recipes) do
    --shutupshutupshutupshutup
    for j=1,#v.outputs,2 do
        local idO = v.outputs[j]
        v.outputs[j] = game_items[idO].name
    end
    for j=1,#v.inputs,2 do
        local idI = v.inputs[j]
        v.inputs[j] = game_items[idI].name
    end
end

local fileN = "recipeListing.py"

local file = io.open(fileN, "w")

if file ~= nil then
    file:write("recipes = {\n")

    for i,v in ipairs(game_recipes) do
        if #v.outputs <= 2 then

            file:write("\t\""..v.name .. "\":\t\t\t\t\t\t[[")
            
            --input names
            for j=1,#v.inputs,2 do
                file:write("\""..v.inputs[j].."\""..(j < #v.inputs-1 and "," or ""))
            end

            file:write("],[")
            --input ammounts
            for j=2,#v.inputs,2 do
                file:write(v.inputs[j]..(j < #v.inputs and "," or ""))
            end

            file:write("],"..v.seconds..","..v.outputs[2].."]" .. (i < #game_recipes and "," or "") .. "\n")

        end
    end
    file:write("}")
    file:close()
else
    print("error loading file")
end

print(count)