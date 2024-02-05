return {
    create_phone_number = function(numbers)
        local s = table.concat(numbers)
        return string.format("(%s) %s-%s", s:sub(1, 3), s:sub(4, 6), s:sub(7))
    end
};
