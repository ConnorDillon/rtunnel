import time
import psutil
from cmdtool import Command


class RTunnel(Command):
    def __init__(self):
        super().__init__(name='rtunnel',
                         description='Reverse SSH tunnel tool',
                         log_fmt='rtunnel: %(levelname)s: %(message)s')
        self.add_arg('lport')
        self.add_arg('rport')
        self.add_arg('target')

    @staticmethod
    def is_same(ps):
        this_ps = psutil.Process()
        if ps.name() == this_ps.name() and ps.cmdline() == this_ps.cmdline():
            return True
        else:
            return False

    def script(self):
        pscount = sum(1 for x in psutil.process_iter() if self.is_same(x))
        if pscount == 1:
            cmd = 'ssh -NR {rport}:localhost:{lport} {target}'
            while True:
                self.info('starting tunnel with command: '+cmd)
                try:
                    self.sh(cmd)
                except KeyboardInterrupt:
                    self.info('keyboard interrupt, exiting')
                    break
                except Exception as e:
                    self.error(self.fmt_exception(e))
                    time.sleep(10)
                finally:
                    self.info('tunnel disconnected')
        elif pscount == 0:
            self.error('script does not recognize itself, check psutil')
        else:
            self.debug('rtunnel already running, exiting')