import unittest
import get_repo
import analyze_repo

class TestPythonRepos(unittest.TestCase):
    def test1(self):
        result = get_repo.r.status_code
        # 判断请求状态码是否正确
        self.assertEqual(result, 200, "请求码错误")

    def test2(self):
        result = len(analyze_repo.repo_dicts)
        # 比较请求数量是否超过需要数量
        self.assertLess(result, 33, "超过所期望的数据数量")

    def test3(self):
        # 检查每个条目中的键是否有name
        result = analyze_repo.repo_dict.keys()
        self.assertIn("name",result,"没有包含所期望的条目")


if __name__ == "__main__":
    # 执行类中所有以test开头的函数，不需要实例化
    unittest.main()
