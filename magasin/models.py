from django.db import models
from datetime import date

# Create your models here.
TYPE_CHOICES=[('em','emballé'),
          ('fr','Frais'),
('cs','Conserve')]

class Produit(models.Model):
    libelle=models.CharField(max_length=100)
    description=models.TextField(default='Non definie')
    prix=models.DecimalField(max_digits=10,decimal_places=3)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True)
    categorie=models.ForeignKey('Categorie',on_delete=models.CASCADE,null=True)
    Fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self) :
        return self.libelle+""+self.description+""+str(self.prix)+""+self.type+""+str(self.categorie)+""+str(self.categorie)
TYPE_CHOICES=[
('Al','Alimentaire'), ('Mb','Meuble'),
('Sn','Sanitaire'), ('Vs','Vaisselle'),
('Vt','Vêtement'),('Jx','Jouets'),
('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')]
class Categorie(models.Model):
    name=models.CharField(max_length=50,default='Alimentaire',choices=TYPE_CHOICES)
    def __str__(self) :
        return self.name
    
class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField(default='Non definie')
    email=models.EmailField(default='Non definie')
    telephone=models.CharField(max_length=8)    
    def __str__(self) :
        return str(self.nom) +" "+str(self.adresse)+" "+str(self.email)+" "+str(self.telephone)
    
class ProduitNC(Produit,models.Model):
    Duree_garantie=models.CharField(max_length= 100)
    def __str__(self):
      return super().__str__() + str(self.Duree_garantie)
    

class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)    
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField("Produit")
    
    def caltot(self):
        total=0
        for produit in self.produits.all():
            total += produit.prix
        return total    

    
    def get_produits_list(self):
        return ", ".join(str(produit) for produit in self.produits.all())
    # def test(self):
    #     ch = ""
    #     for p in self.produits.all():
    #         ch = ch + str(p) + " "
    #     return ch
    def __str__(self):
        return super().__str__() + str(self.dateCde)+ str(self.totalCde)+str(self.caltot())+str(self.get_produits_list())