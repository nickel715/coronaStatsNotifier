def _find_nth(haystack: str, needle: str, n: int):
    offset = 0
    while offset >= 0 and n > 0:
        offset = haystack.find(needle, offset + 1)
        n -= 1

    return offset


class Parser:
    INCIDENCE_POSITION = 7

    @staticmethod
    def find_incidence(content: str) -> str:
        needle = '"text":"'
        offset = _find_nth(content, needle, Parser.INCIDENCE_POSITION)

        num_start = offset + len(needle)
        num_end = content.find('"', num_start)

        return content[num_start:num_end]

    @staticmethod
    def find_updated(content: str) -> str:
        needle = 'Stand: '
        start = content.find(needle) + len(needle)
        end = content.find(' |', start)

        return content[start:end]
