from ropevim import _interface
from ropemode.interface import _CodeAssist
from rope.base.exceptions import BadIdentifierError
import vim

class Completer(object):
    def create_code_assist(self):
        return _CodeAssist(_interface, _interface.env)

    def __call__(self, findstart, base):
        try:
            if findstart:
                self.code_assist = self.create_code_assist()
                base_len = self.code_assist.offset - \
                           self.code_assist.starting_offset
                return int(vim.eval("col('.')")) - base_len - 1
            else:
                try:
                    proposals = self.code_assist._calculate_proposals()
                except Exception:
                    return []
                if vim.eval("complete_check()") != "0":
                    return []
                ps = []
                for proposal in proposals:
                    ci = _interface.env._completion_text(proposal)
                    #vim.command('echo "%s"' % ci)
                    #vim.command('echoerr "%s"' % proposal)
                    #vim.command('echoerr "%s"' % proposal.__class__)
                    #vim.command("call complete_add(%r)" % ci)
                    #vim.command('echoerr "%s"' % proposal.parameters)
                    p = {}
                    args = proposal.parameters or []
                    p['word'] = "%s(" % ci
                    p['info'] = proposal.get_doc() or 'x.' + str(ci) + '(' + ', '.join(map(str, args)) + ')'
                    p['abbr'] = ci
                    ps.append(p)
                del self.code_assist
                return ps
                return [{"info": "Dit is een mooie test!", "word": "toets(", "abbr": "toets()"}, {"info": "Lekker!", "word": "lekka(", "abbr": "lekka()    and maybe some args, tester"}]
                return []
        except BadIdentifierError:
            del self.code_assist
            if findstart:
                return -1
            else:
                return []
