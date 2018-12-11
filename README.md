# CommandLauncher
GUI to help you launch powershell/batch/sqlcmd commands remotely.
Querry or batch commands on top pane passed for every destination at left pane by using method specified at dropdown list.
On the bottom pane command output will be visible after launch in a LIFO fashion.
User name and password passed for database/user login which can be left empty or unedited to start methods without any credentials except for sqlcmd.
While using sqlcmd mode if no password specified at database side please use "" as password.

Multithreading used, thread pool increases due to stack space optimization on the run.

![alt text](https://image.ibb.co/iLY12A/Capture22.jpg)

#### Dependencies:

sqlcmd at host (should be available at $env)

powershell 1.0 at both host and destination system (for PS methods)

PSEXEC.exe at same folder with executable (for PSEXEC mode)

--CommandLauncher.exe is enough to start application without build files

###### THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
