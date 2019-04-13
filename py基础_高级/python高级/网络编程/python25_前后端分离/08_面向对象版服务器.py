# 静态服务器显示一个hello world

# 1. 创建一个tcp服务器
# 2.循环接收客户端请求
# 3. 处理客户端的请求
# 4.关闭
import socket
import threading

import mini_web_08


class WebServer(object):
	def client_exec(self, client):
		"""
		客户端的处理
		:param client: 与之对应的客户端
		:return: NONE
		"""
		# 根据不同的地址返回不同的数据
		# 1.接收请求数据
		# 2.请求资源的地址获取
		# 3.根据地址判断返回不同的数据
		# 4.关闭

		# 1.接收请求数据
		data = client.recv(1024)
		# 不要相信别人传的任何的数据
		if data:
			# 说明有数据
			# 解析到对应的地址
			client_data = data.decode("utf-8")
			print(client_data)
			# 请求的数据
			request_data_list = client_data.split(" ", maxsplit=2)
			print(request_data_list)

			try:
				# 得到路径
				file_path = request_data_list[1]

				# 判断一下如果是/那么就/index.html
				if file_path == "/":
					file_path = "/index.html"
			except Exception as e:
				print("异常:", e)
				# 关闭退出
				client.close()
				return

		else:
			# 说明没有数据
			# 关闭返回
			client.close()
			return

		# 根据资源的特性可以分为静态与动态,python程序员能不能进行代码修改的
		# 如果你是.html后缀那是动态的,我必须一个网页都独立的进行处理
		# 如果你是静态的那么我只要读返回就可以了

		if file_path.endswith(".html"):
			# 根据不同的地址返回不同的响应体
			# 响应行
			# response_line = "HTTP/1.1 200 OK\r\n"

			# 响应头
			response_head = ""

			# 空行
			response_empty = "\r\n"

			# 得到业务的数据
			response_line, response_head, response_body = mini_web_08.application(file_path)

			# 发送动态的资源了
			response_content = response_line + response_head + response_empty + response_body

			# 发送
			client.send(response_content.encode("utf-8"))

		else:
			try:
				# 图片,mp3,mp4其他的一切程序不能改的静态资源,我们应该统一的进行处理,就是打开返回
				with open("./static%s" % file_path, 'rb') as f:
					content = f.read()

				# 响应行
				response_line = "HTTP/1.1 200 OK\r\n"

				# 响应头
				response_head = ""

				# 空行
				response_empty = "\r\n"

				# 响应体
				response_body = content

				# 响应内容
				response_content = response_line.encode("utf-8") + response_head.encode(
					"utf-8") + response_empty.encode(
					"utf-8") + response_body

				# 发送内容
				client.send(response_content)

			except Exception as e:
				print("异常", e)
				# 找不到网页
				response_line = "HTTP/1.1 404 NOT FOUND\r\n"

				# 响应头
				response_head = ""

				response_body = ""  # 静态资源可以不用写

				# 空行
				response_empty = "\r\n"

				response_content = response_line + response_head + response_empty + response_body

				# 编码发送
				client.send(response_content.encode("utf-8"))
				# 关闭
				client.close()
				return

		# 关闭
		client.close()

	def run_server(self):
		while True:
			client, address = self.socket_server.accept()

			# 3. 处理客户端的请求
			# self.client_exec(client)

			# 把客户端的处理加入到线程中
			thread_client = threading.Thread(target=self.client_exec, args=(client,),daemon=True)

			# thread_client.setDaemon(True)
			# 开启
			thread_client.start()

		# 4.关闭
		socket_server.close()

	# 这个在写类本身方法
	def __init__(self):
		# 1.1 初始化socket
		self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# 1.2 绑定 端口
		self.socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
		self.socket_server.bind(("", 8080))
		# 1.3 监听模式
		self.socket_server.listen(128)


# 入口函数
# 必须简洁像书的目录 一样
def main():
	"""web服务器"""
	# 服务器初始化
	server = WebServer()

	# 开启服务
	server.run_server()


if __name__ == '__main__':
	main()
