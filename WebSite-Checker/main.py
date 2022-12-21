#Web site checker
#Author: Arslon Erkinov
#Enter websites as http(s)://www.yourwebsite.com

import urllib.request
import tkinter as tk


def Web_check():
  window = tk.Tk()
  window.geometry('400x200')
  head = tk.Label(window, text='Website Connectivity Checker',font=('Calibri 15'))
  head.pack(pady=10)

  def check_url():
      web = (url.get())
      status_code = urllib.request.urlopen(web).getcode()
      website_is_up = status_code == 200

      if website_is_up:
          tk.Label(window, text='Website Available',font=('Calibri 15')).place(x=95, y=100)
      else:
          tk.Label(window, text='Website Not Available',font=('Calibri 15')).place(x=95, y=100)

  url = tk.StringVar()
  tk.Entry(window, textvariable=url).place(x=50, y=60, height=20, width=280)
  tk.Button(window, text='Check', command=check_url).place(x=340, y=60)
  window.mainloop()


if __name__ == '__main__':
   Web_check()


