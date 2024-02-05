return {
    create_phone_number = function(numbers)
        return string.format("(%s%s%s) %s%s%s-%s%s%s%s", table.unpack(numbers))
    end
};
