package com.example.finalexam;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ActionBar actionBar = getSupportActionBar();
        actionBar.hide();

        Button login = findViewById(R.id.loginBtn);
        EditText id = findViewById(R.id.id);
        EditText pw = findViewById(R.id.password);
        TextView jo = findViewById(R.id.jo);

        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
//                Toast.makeText(MainActivity.this, idC, Toast.LENGTH_SHORT).show();
                Intent getIntent = getIntent();
                String idG = getIntent.getExtras().get("id").toString();
                String pwG = getIntent.getExtras().get("pw").toString();
                String nickG = getIntent.getExtras().get("nickname").toString();
                String emailG = getIntent.getExtras().get("email").toString();

                String idC = id.getText().toString();
                String pwC = pw.getText().toString();

                if(idC.isEmpty()){
                    Toast.makeText(MainActivity.this, "아이디를 입력해주세요", Toast.LENGTH_SHORT).show();
                }else if(pwC.isEmpty()){
                    Toast.makeText(MainActivity.this, "비밀번호를 입력해주세요", Toast.LENGTH_SHORT).show();
                }else if(idG.equals(idC) && pwG.equals(pwC)) {
                    Intent intent = new Intent(MainActivity.this, login.class);
                    intent.putExtra("id", idG);
                    intent.putExtra("password", pwG);
                    intent.putExtra("nick", nickG);
                    intent.putExtra("email", emailG);
                    startActivity(intent);
                } else {
                    Toast.makeText(MainActivity.this, "아이디나 비밀번호를 입력해주세요", Toast.LENGTH_SHORT).show();
                }
            }
        });

        jo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intentJ = new Intent(MainActivity.this, join.class);
                startActivity(intentJ);
            }
        });
    }
}