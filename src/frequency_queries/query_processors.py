class QueryProcessor:

    def __init__(self, element, storage_keeper):
        self.element = element
        self.storage_keeper = storage_keeper

    def execute(self):
        pass


class AppendingProcessor(QueryProcessor):

    def execute(self):
        curr_elem_freq = self.storage_keeper.freq_dict.get(self.element, 0)
        new_elem_freq = curr_elem_freq + 1
        self.storage_keeper.freq_dict[self.element] = new_elem_freq

        curr_freq_freq = self.storage_keeper.total[curr_elem_freq]
        if curr_freq_freq == 1:
            self.storage_keeper.total.pop(curr_elem_freq)
        else:
            self.storage_keeper.total[curr_elem_freq] = curr_freq_freq - 1

        self.storage_keeper.total[new_elem_freq] = self.storage_keeper.total.get(new_elem_freq, 0) + 1

        return None


class RemovingProcessor(QueryProcessor):

    def execute(self):
        curr_elem_freq = self.storage_keeper.freq_dict.get(self.element, 0)
        new_elem_freq = curr_elem_freq - 1
        self.storage_keeper.freq_dict[self.element] = new_elem_freq

        actualize_maps(self.storage_keeper.total, curr_elem_freq)

        curr_freq_freq = self.storage_keeper.total[curr_elem_freq]
        if curr_freq_freq == 1:
            self.storage_keeper.total.pop(curr_elem_freq)
        else:
            self.storage_keeper.total[curr_elem_freq] = curr_freq_freq - 1

        self.storage_keeper.total[new_elem_freq] = self.storage_keeper.get(new_elem_freq, 0) + 1

        return None


class CountingProcessor(QueryProcessor):

    def execute(self):
        fptr = open('C:/tmp/lel.txt', 'a+')

        fptr.write('KEK\n')
        fptr.write(str(self.storage_keeper.freq_dict) + '\n')
        fptr.write(str(self.storage_keeper.total) + '\n')

        fptr.close()
        return 1 if self.storage_keeper.total.get(self.element, 0) > 0 else 0


def actualize_maps(dictionary_from, element):
    current_value = dictionary_from.get(element, 0)
    if current_value == 1:
        dictionary_from.pop(current_value)
    elif current_value > 1:
        dictionary_from[element] = current_value - 1

