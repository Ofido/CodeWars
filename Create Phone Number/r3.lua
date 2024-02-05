local solution = {}

function solution.create_phone_number(numbers)
    return ("(%d%d%d) %d%d%d-%d%d%d%d"):format(table.unpack(numbers))
end

return solution
