#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <string.h>
#include <cstdio>
#include <cstdlib>

using namespace std;
typedef long long ll;

ll getvarno(ll n2, ll j, ll i)
{
	return (n2*j + i + 1);
}

struct pairhash {
public:
  template <typename T, typename U>
  std::size_t operator()(const std::pair<T, U> &x) const
  {
    return std::hash<T>()(x.first) ^ std::hash<U>()(x.second);
  }
};



int main(int argc, char *argv[])
{
	ifstream infile;
	infile.open(strcat(argv[1],".graphs"));
	if (infile.is_open())
	{
		std::unordered_map<ll,ll> N1; // small graph
		std::unordered_map<ll,ll> N2; // large graph

		std::vector<std::pair<ll,ll> > SN1;
		std::vector<std::pair<ll,ll> > SN2;
		string line;
		int j = 1;
		
		getline(infile, line);

		while (line != "0 0")
		{
			int x = line.find(' ');
			ll x1 = stoi(line.substr(0,x));
			ll x2 = stoi(line.substr(x+1));
			SN2.push_back(std::make_pair(x1,x2));
			if (N2.find(x1) == N2.end())
			{
				N2[x1]= j;
				j ++;
			}
			if (N2.find(x2) == N2.end())
			{
				N2[x2] = j;
				j ++;
			}
			getline(infile, line);
		}

		j = 1;

		while (getline(infile, line))
		{
			int x = line.find(' ');
			ll x1 = stoi(line.substr(0,x));
			ll x2 = stoi(line.substr(x+1));
			SN1.push_back(std::make_pair(x1,x2));
			if (N1.find(x1) == N1.end())
			{
				N1[x1]= j;
				j ++;
			}
			if (N1.find(x2) == N1.end())
			{
				N1[x2] = j;
				j ++;
			}
		}

		ll n2 = N2.size();
		ll n1 = N1.size();

		vector<vector<bool> > EdgesG1 (n1, std::vector<bool> (n1, false));
		std::vector<std::vector<bool> > EdgesG2 (n2, std::vector<bool> (n2, false));

		std::vector<ll> AdjG2_out (n2);
		std::vector<ll> AdjG1_out (n1);
		std::vector<ll> AdjG2_in (n2);
		std::vector<ll> AdjG1_in (n1);


		for (int i = 0 ; i < SN2.size() ; i ++)
		{
			ll x = N2[SN2[i].second];
			ll y = N2[SN2[i].first];
			AdjG2_in[ x - 1] ++;
			AdjG2_out[ y - 1] ++;
			EdgesG2[y-1][x-1] = true;
		}

		for (int i = 0 ; i < SN1.size() ; i ++)
		{
			ll x = N1[SN1[i].first];
			ll y = N1[SN1[i].second];
			AdjG1_out[x - 1] ++;
			AdjG1_in[y - 1] ++;
			EdgesG1[x-1][y-1]= true;
		}

		ofstream fout;
		fout.open("var_mapping.txt");
		for (auto it = N1.begin() ; it != N1.end() ; it ++)
			fout << (*it).second << " " << (*it).first << std::endl;
		fout << "-1\n";
		for (auto it = N2.begin() ; it != N2.end() ; it ++)
			fout << (*it).second << " " << (*it).first << std::endl;

		fout.close();

		// file ready.
		FILE * fp;
		fp = fopen(strcat((argv[1]) , ".satinput"),"w");
		// ffout.open();
		fprintf(fp, "p cnf %lld %lld\n", n1*n2, (n1 + n1*(n2*(n2-1))/2 + n2*(n1*(n1-1))/2 + n1*(n1-1)*n2*(n2-1)/4));


		std::unordered_set<pair<ll,ll>, pairhash > NotPoss;
		for (int i = 0 ; i < n1 ; i ++)
		{
			for (int j = 0 ; j < n2 ; j ++)
			{
				if (AdjG2_out[j] < AdjG1_out[i] || AdjG2_in[j] < AdjG1_in[i])
					NotPoss.insert(std::make_pair(i,j));
			}
		}

		for (int i = 0 ; i < n1 ; i ++)
		{
			string s = "";
			for (int j = 0 ; j < n2 ; j ++)
			{
				std::pair<ll,ll> p = std::make_pair(i,j);
				if (NotPoss.find(p) == NotPoss.end())
					s += "-" + to_string(getvarno(n2,i,j)) + " ";
			}
			s += "0\n";
			fprintf(fp, "%s", s.c_str());
		}

		for (int i = 0 ; i < n1 ; i ++)
		{
			for (int j = 0 ; j < n2 ; j ++)
			{
				for (int k = j+1 ; k < n2 ; k ++)
				{
					pair<ll,ll> p1 = std::make_pair(i,j);
					pair<ll,ll> p2 = std::make_pair(i,k);
					if (NotPoss.find(p1) == NotPoss.end() && NotPoss.find(p2) == NotPoss.end())
						fprintf(fp, "%lld %lld 0\n", getvarno(n2,i,j), getvarno(n2,i,k));
				}
			}
		}

		for (int i = 0 ; i < n2 ; i ++)
		{
			for (int j = 0 ; j < n1 ; j ++)
			{
				for (int k = j+1 ; k < n1  ; k ++)
				{
					pair<ll,ll> p1 = std::make_pair(j,i);
					pair<ll,ll> p2 = std::make_pair(k,i);
					if (NotPoss.find(p1) == NotPoss.end() && NotPoss.find(p2) == NotPoss.end())
						fprintf(fp, "%lld %lld 0\n", getvarno(n2,j,i), getvarno(n2,k,i));
				}
			}
		}

		for (int i = 0 ; i < n1 ; i ++)
		{
			for (int j = 0 ; j < n1 ; j ++)
			{
				if (i != j)
				{
					for (int k = 0 ; k < n2 ; k ++)
					{
						for (int l = 0 ; l < n2 ; l ++)
						{
							if (k != l)
							{
								pair<ll,ll> ik = std::make_pair(i,k);
								pair<ll,ll> jl = std::make_pair(j,l);
								if (EdgesG2[k][l] != EdgesG1[i][j] && NotPoss.find(ik) == NotPoss.end() && NotPoss.find(jl) == NotPoss.end())
									fprintf(fp, "%lld %lld 0\n", getvarno(n2,i,k), getvarno(n2,j,l));
							}
						}
					}
				}
			}
		}

		fclose(fp);
		infile.close();
	}
	return 0;
}