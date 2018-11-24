# querylauncher
GUI to help you launch sqlcmd commands.
List taken from left pane for sqlcmd -S switch and querry on top pane passed for every destination at left pane.
On the bottom pane querry output will be visible after launch in a LIFO fashion.
User name and password passed to -U and -P switch for database login.
If no password specified at database side please use "" as password.

Multithreading used, thread pool increases due to stack space optimization on the run.

![alt text](https://image.ibb.co/iLY12A/Capture22.jpg)

Dependencies:
-sqlcmd (available at $env)

-querrylauncher.exe is enough to start application without build files

###### THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
