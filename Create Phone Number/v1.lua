return {
    create_phone_number = function(numbers)
        local output = string.format("(%d%d%d) %d%d%d-%d%d%d%d", numbers[1], numbers[2], numbers[3], numbers[4],
            numbers[5], numbers[6], numbers[7], numbers[8], numbers[9], numbers[10])
        do return output end
    end
};
